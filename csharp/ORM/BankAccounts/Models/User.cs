using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace BankAccounts.Models
{
    [Table("users")]
    public class User
    {
       [Key]
        public int userID{get;set;}
        [Required(ErrorMessage="Please enter your First Name")]
        [MinLength(2)]
        public string FirstName{get;set;}
        [Required(ErrorMessage="Please enter your Last Name")]
        [MinLength(2)]
        public string LastName{get;set;}
        [Required(ErrorMessage="Please enter your Email Address")]
        [EmailAddress]
        public string Email{get;set;}
        [Required(ErrorMessage="Please enter a password")]
        [MinLength(8, ErrorMessage ="Password must be 8 characters or longer.")]
        [DataType(DataType.Password)]
        public string Password{get;set;}
        [Required(ErrorMessage="Please confirm your password.")]
        [Compare("Password")]
        [NotMapped]
        public string ConfPassword{get;set;}
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;
       
    }

    public class LogUser
    {
        [EmailAddress]
        [Required(ErrorMessage="Email Address is required")]
        public string Email {get;set;}
        [Required(ErrorMessage="Password is required")]
        [DataType(DataType.Password)]
        public string Password{get;set;}
    }
}