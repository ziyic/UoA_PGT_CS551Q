from django.test import TestCase
import random


# Create your tests here.


class MainTest(TestCase):
    def test_index(self):
        """
        Test the index page, whose title is Global Fire Emissions, used template fires/index.html.
        :return:
        """
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "<title>Global Fire Emissions</title>")
        self.assertTemplateUsed(res, "fires/index.html")

    def test_region_list(self):
        """
        Test if region list page works.
        :return:
        """

        page_num = random.randint(1, 7)
        res_region_list = self.client.get(f'/regions?page={page_num}')
        self.assertEqual(res_region_list.status_code, 200)
        self.assertContains(res_region_list, page_num)
        self.assertTemplateUsed(res_region_list, "fires/regions.html")
        # test passed

    def test_region_detail(self):
        """
        Test region detail page.
        Attention: if you want to test function "get_object_or_404()", you need to test with a valid id and an invalid
        id.
        :return:
        """
        valid_id = random.randint(1, 5)
        invalid_id = random.randint(-5, -1)
        # invalid test
        invalid_res = self.client.get(f"/region/{invalid_id}")
        self.assertEqual(invalid_res.status_code, 404)
        # valid test
        valid_res = self.client.get(f"/region/{valid_id}")
        self.assertEqual(valid_res.status_code, 200)
        self.assertTemplateUsed(valid_res, "fires/region_details.html")
        self.assertContains(valid_res, valid_id)

    def test_fire_detail_by_year(self):
        """
        Test fire detail by year page.
        Attention: All tests can ONLY test your page returns. Data checks not included.
        Also, replace code below to test your functions controlling database works correctly.
        :return:
        """
        test_regions = ["China", "Australia", "United Kingdom of Great Britain and Northern Ireland"]
        random_region = random.choice(test_regions)
        random_year = random.randint(2010, 2020)
        res = self.client.get('/fire/{}/{}'.format(random_region, random_year))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, random_year)
        self.assertContains(res, random_region)
        self.assertTemplateUsed(res, "fires/fire_year.html")

    def test_fire_detail_by_type(self):
        """
        Test fire detail by type page.
        :return:
        """
        test_regions = ["China", "Australia", "United Kingdom of Great Britain and Northern Ireland"]
        test_types = ["TCC_All_fires", "TCC_TEMF_Fires", "TCC_AGRI_fires",
                      "Total_Area_Burned", "TCC_DEFO_fires", "TCC_SAVA_Fires"]
        random_region = random.choice(test_regions)
        random_type = random.choice(test_types)
        res = self.client.get(f"/fire/{random_region}/{random_type}")
        self.assertContains(res, random_type)
        self.assertContains(res, random_region)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "fires/fire_type.html")
        # test passed
