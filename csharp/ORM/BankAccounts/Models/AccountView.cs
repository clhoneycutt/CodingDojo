using System.Collections.Generic;
using BankAccounts.Models;

namespace BankAccounts
{
    public class AccountView  
    {  
        public IEnumerable<Transaction> Transactions { get; set; }  
        public Transaction Transaction { get; set; }
    }  
}