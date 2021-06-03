import os
import shutil
import unittest
import tempfile
from pathlib import Path

from fds.services.dvc_service import DVCService
from fds.services.fds_service import FdsService
from fds.services.git_service import GitService


class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.repo_path = tempfile.mkdtemp()
        self.git_service = GitService(self.repo_path)
        self.dvc_service = DVCService(self.repo_path)
        self.fds_service = FdsService(self.git_service, self.dvc_service)
        os.chdir(self.repo_path)

    def tearDown(self):
        super().tearDown()
        shutil.rmtree(self.repo_path)

    def create_fake_git_data(self):
        git_path = f"{self.repo_path}/git_data"
        Path(git_path).mkdir(parents=True, exist_ok=True)
        # Creating 5 random files
        for i in range(0,5):
            self.create_dummy_file(f"{git_path}/file-{i}", 10)

    def create_dummy_file(self, file_name: str, size: int):
        with open(file_name, 'wb') as fout:
            fout.write(os.urandom(size))

