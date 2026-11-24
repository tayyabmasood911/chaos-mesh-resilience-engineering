import os
import unittest
import yaml

class TestChaosMeshResilienceSuite(unittest.TestCase):
    def test_core_files_exist(self):
        required_files = [
            "README.md",
            "Makefile",
            "SECURITY.md",
            ".gitattributes",
            ".github/workflows/ci.yml",
            "scripts/healthcheck.sh",
            "scripts/chaos_runner.py",
            "scripts/run_experiments.sh",
            "config/production.env.example",
            "pod-kill-chaos.yaml",
            "network-delay-experiment.yaml",
            "manifests/pod-kill-chaos.yaml",
            "manifests/network-chaos.yaml",
            "manifests/stress-chaos.yaml",
            "manifests/http-chaos.yaml",
            "manifests/workflow-chaos.yaml",
            "docs/architecture.svg"
        ]
        for file_path in required_files:
            self.assertTrue(os.path.exists(file_path), f"Missing required file: {file_path}")

    def test_crd_manifest_structures(self):
        manifests = [
            ("pod-kill-chaos.yaml", "PodChaos"),
            ("network-delay-experiment.yaml", "NetworkChaos"),
            ("manifests/pod-kill-chaos.yaml", "PodChaos"),
            ("manifests/network-chaos.yaml", "NetworkChaos"),
            ("manifests/stress-chaos.yaml", "StressChaos"),
            ("manifests/http-chaos.yaml", "HTTPChaos"),
            ("manifests/workflow-chaos.yaml", "Workflow")
        ]
        for filename, expected_kind in manifests:
            with open(filename, "r", encoding="utf-8") as f:
                doc = yaml.safe_load(f)
            self.assertEqual(doc.get("apiVersion"), "chaos-mesh.org/v1alpha1")
            self.assertEqual(doc.get("kind"), expected_kind)
            self.assertIn("metadata", doc)
            self.assertIn("spec", doc)

    def test_architecture_diagram_white_theme(self):
        with open("docs/architecture.svg", "r", encoding="utf-8") as f:
            svg = f.read()
        self.assertIn('fill="#ffffff"', svg, "Must have pure white background")
        self.assertIn("Chaos Mesh", svg)

if __name__ == "__main__":
    unittest.main()
