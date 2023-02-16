from django.test import TestCase
from portfolio.models import Project

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title="Proyecto 1", description="Descripción del proyecto 1", url_git="https://github.com/proyecto1", url_deploy="https://proyecto1.com")

    def test_title_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

        max_length = project._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_description_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

        max_length = project._meta.get_field('description').max_length
        self.assertEquals(max_length, 400)

    def test_url_git_blank(self):
        project = Project.objects.get(id=1)
        blank = project._meta.get_field('url_git').blank
        self.assertTrue(blank)

    def test_url_deploy_blank(self):
        project = Project.objects.get(id=1)
        blank = project._meta.get_field('url_deploy').blank
        self.assertTrue(blank)

        null = project._meta.get_field('url_deploy').null
        self.assertTrue(null)

        help_text = project._meta.get_field('url_deploy').help_text
        self.assertIn("opcional", help_text)
