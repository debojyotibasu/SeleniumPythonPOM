import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.NewCarsPage import NewCarsPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class Test_Carwale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("*************:Inside New Car Test:*************")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand, carTitle", dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("*************:Select Car Test started:*************")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car Brand is: ", carBrand)
        # home.gotoNewCars()
        # newCar = NewCarsPage(self.driver)
        # newCar.selectBMW()

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyudai()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"

    @pytest.mark.parametrize("carBrand, carTitle", dataProvider.get_data("NewCarsTest"))
    def test_printCarNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("*************:Select Car Names and Prices Test started:*************")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        print("Car Brand is: ", carBrand)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
            car.getCarNamesAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
            car.getCarNamesAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyudai()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
            car.getCarNamesAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the current page as title is not matching"
            car.getCarNamesAndPrices()

        time.sleep(3)