using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BankAccounts.Models
{
    public class Transaction
    {
        [Key]
        public int TransactionID {get;set;}
        [Required]
        public int AccountHolderID {get;set;}
        [Required]
        [RegularExpression("^[$]?-?[0-9]*(.)?[0-9]?[0-9]?$", ErrorMessage="Please enter a valid number")]
        public float Amount {get;set;}
        public DateTime CreatedAt {get;set;} = DateTime.Now;

        public User AccountHolder {get;set;}
    }
}