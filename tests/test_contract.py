# Kind: offline package contract tests. Trigger: explicit unittest command in README.
import re
import subprocess
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class PackageContract(unittest.TestCase):
    def test_one_discovery_root(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md')], ['SKILL.md'])

    def test_root_metadata(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        header = text.split('---', 2)[1]
        self.assertRegex(header, r'(?m)^name: skillify$')
        description = re.search(r'(?m)^description: (.+)$', header)
        self.assertIsNotNone(description)
        self.assertGreater(len(description[1]), 60)

    def test_bundled_links_stay_inside_package_and_exist(self):
        for file in ROOT.rglob('*.md'):
            if '.git' in file.parts:
                continue
            text = re.sub(r'```[\s\S]*?```', '', file.read_text(encoding='utf-8'))
            for target in re.findall(r'\]\(([^\s)]+)\)', text):
                if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                    continue
                resolved = (file.parent / unquote(target.split('#')[0])).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (file.name, target))
                self.assertTrue(resolved.exists(), (file.name, target))

    def test_real_overlay_is_ignored(self):
        for name in ['local/settings.md', 'settings.local.json', 'examples/private-overlay.md']:
            result = subprocess.run(['git', '-C', str(ROOT), 'check-ignore', '--no-index', '-q', name])
            self.assertEqual(result.returncode, 0, name)

    def test_example_is_a_complete_output_contract(self):
        text = (ROOT / 'examples/csv-review.md').read_text(encoding='utf-8')
        for requirement in ['item_id,status,reason', 'input record order', 'one output row per input record', 'do not write a success report']:
            self.assertIn(requirement, text)

    def test_no_runtime_install_required(self):
        self.assertFalse((ROOT / 'package.json').exists())
        self.assertTrue((ROOT / 'LICENSE').is_file())
        self.assertTrue((ROOT / 'SOURCES.md').is_file())


if __name__ == '__main__':
    unittest.main()
