# accounting/models.py
from django.db import models

class Account(models.Model):
    EX_TYPE_CHOICES = [
        ('Accounts Payable Vendor', 'Accounts Payable Vendor'),
        ('Account Receivable', 'Account Receivable'),
        ('Administrative Expenses', 'Administrative Expenses'),
        ('Administrative Income', 'Administrative Income'),
        ('Advance Against Expense', 'Advance Against Expense'),
        ('Advance Against Salary', 'Advance Against Salary'),
        ('Advance Deposit and Prepayments', 'Advance Deposit and Prepayments'),
        ('Advance To Employee', 'Advance To Employee'),
        ('Advance To Personnel', 'Advance To Personnel'),
        ('Bank Expenses', 'Bank Expenses'),
        ('Bank Overdraft', 'Bank Overdraft'),
        ('Cash and Cash Equivalents', 'Cash and Cash Equivalents'),
        ('Cash In Hand', 'Cash In Hand'),
        ('Depreciation and Amortization', 'Depreciation and Amortization'),
        ('Director Loan', 'Director Loan'),
        ('Direct Expense', 'Direct Expense'),
        ('Direct Overhead', 'Direct Overhead'),
        ('Direct Purchase', 'Direct Purchase'),
        ('Drawings', 'Drawings'),
        ('Factory Building', 'Factory Building'),
        ('Financial Expenses', 'Financial Expenses'),
        ('Furniture and Fixture', 'Furniture and Fixture'),
        ('Import Expense', 'Import Expense'),
        ('Income From Additional Sales', 'Income From Additional Sales'),
        ('Income From Bank', 'Income From Bank'),
        ('Income From Others', 'Income From Others'),
        ('Inter Company Accounts', 'Inter Company Accounts'),
        ('Investment', 'Investment'),
        ('Lc Margin', 'Lc Margin'),
        ('Lc Purchase', 'Lc Purchase'),
        ('Loan Given To Personel', 'Loan Given To Personel'),
        ('Long Term Unsecured', 'Long Term Unsecured'),
        ('Motor Vehicle', 'Motor Vehicle'),
        ('Office Building', 'Office Building'),
        ('Office Equipment', 'Office Equipment'),
        ('Old Accounts Receivable', 'Old Accounts Receivable'),
        ('Opening Stock', 'Opening Stock'),
        ('Other Advance', 'Other Advance'),
        ('Other Liabilities', 'Other Liabilities'),
        ('Other Non-current Assets', 'Other Non-current Assets'),
        ('Paid Up Capital', 'Paid Up Capital'),
        ('Payable Load Bill', 'Payable Load Bill'),
        ('Payable Unload Bill', 'Payable Unload Bill'),
        ('Petty Cash', 'Petty Cash'),
        ('Plant And Equipments', 'Plant And Equipments'),
        ('Property Land And Building', 'Property Land And Building'),
        ('Provision For Expense', 'Provision For Expense'),
        ('Purchase', 'Purchase'),
        ('Renovation And Subscription', 'Renovation And Subscription'),
        ('Reserve Fund', 'Reserve Fund'),
        ('Retained Earnings', 'Retained Earnings'),
        ('Selling And Marketing Expense', 'Selling And Marketing Expense'),
        ('Sales', 'Sales'),
        ('Sales Return', 'Sales Return'),
        ('Security Deposit', 'Security Deposit'),
        ('Share Holders Loan', 'Share Holders Loan'),
        ('Share Money Deposit', 'Share Money Deposit'),
        ('Spare Parts', 'Spare Parts'),
        ('Sundry Creditors', 'Sundry Creditors'),
        ('Trade In Transit', 'Trade In Transit'),
        ('Trade Receivable', 'Trade Receivable'),
        ('Truck and Loary', 'Truck and Loary'),
    ]
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    account_id = models.CharField(max_length=50, unique=True)
    ex_type = models.CharField(max_length=100, choices=EX_TYPE_CHOICES)
    account_title = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20, blank=True)
    district = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    account_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_id} - {self.account_title}"