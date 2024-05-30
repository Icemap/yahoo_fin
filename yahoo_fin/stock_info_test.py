import numpy as np
import unittest

import stock_info as s


class StockInfoOptions(unittest.TestCase):

    def test_get_income_statement(self):
        df = s.get_income_statement('IBM', yearly=True)
        self.__test_not_empty_and_has_index(df, ['totalRevenue'])

    def test_get_balance_sheet(self):
        df = s.get_balance_sheet('IBM', yearly=True)
        self.__test_not_empty_and_has_index(df, ['endDate'])

    def test_get_cash_flow(self):
        df = s.get_cash_flow('IBM', yearly=True)
        print(df.index)
        self.__test_not_empty_and_has_index(df, ['endDate', 'netIncome'])

    def test_get_financials(self):
        result = s.get_financials('IBM', yearly=True)
        df = result['yearly_income_statement']
        self.__test_not_empty_and_has_index(
            df, ['endDate', 'totalRevenue', 'costOfRevenue', 'grossProfit',
                 'researchDevelopment', 'sellingGeneralAdministrative', 'nonRecurring',
                 'otherOperatingExpenses', 'totalOperatingExpenses', 'operatingIncome',
                 'totalOtherIncomeExpenseNet', 'ebit', 'interestExpense',
                 'incomeBeforeTax', 'incomeTaxExpense', 'minorityInterest',
                 'netIncomeFromContinuingOps', 'discontinuedOperations',
                 'extraordinaryItems', 'effectOfAccountingCharges', 'otherItems',
                 'netIncome', 'netIncomeApplicableToCommonShares'])

    def test_get_earnings(self):
        df = s.get_earnings('IBM')['yearly_revenue_earnings']
        self.assertFalse(df.empty, "Earnings statement should not be empty")
        self.assertIn('revenue', df.columns, "Earnings statement should have 'revenue' column")

    def test_get_company_info(self):
        df = s.get_company_info('IBM')
        self.assertFalse(df.empty, "Company info statement should not be empty")
        self.assertIn('industry', df.index, "Company info statement should have 'industry' index")

    def test_get_company_officers(self):
        df = s.get_company_officers('IBM')
        self.assertFalse(df.empty, "Company officers statement should not be empty")
        self.assertIn('age', df.columns, "Company officers statement should have 'age' column")

    def test_get_live_price(self):
        price = s.get_live_price('IBM')
        self.assertTrue(np.dtype('float64') == price.dtype, "Price should not be a float64 number")

    def __test_not_empty_and_has_index(self, df, check_indexes):
        self.assertFalse(df.empty, "Dataframe should not be empty")
        for check_index in check_indexes:
            self.assertIn(check_index, df.index, f"Dataframe should have '{check_index}' index")
