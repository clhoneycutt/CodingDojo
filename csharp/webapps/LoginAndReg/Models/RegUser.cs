using System;
using System.ComponentModel.DataAnnotations;

namespace LoginAndReg.Models
{
    public class RegUser
    {  
        [Required]
        [MinLength(2)]
        public string FirstName {get;set; }
        [Required]
        [MinLength(2)]
        public string LastName { get;set; }
        [Required]
        [DataType(DataType.EmailAddress)]
        public string Email { get;set; }
        [Required]
        [DataType(DataType.Password)]
        [MinLength(8)]
        public string Password { get;set; }
        [Required]
        [Compare("Password")]
        [DataType(DataType.Password)]
        public string ConfirmPassword { get;set; }
    }
}