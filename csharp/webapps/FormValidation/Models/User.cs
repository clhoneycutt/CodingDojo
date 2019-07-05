using System;
using System.ComponentModel.DataAnnotations;

namespace FormValidation.Models
{
    public class User
    {
        [Required]
        [MinLength(4)]
        public string FirstName {get;set;}
        [Required]
        [MinLength(4)]
        public string LastName {get;set;}
        [Required]
        [Range(1,120)]
        public int Age {get;set;}
        [Required]
        [MinLength(3)]
        [DataType(DataType.EmailAddress)]
        public string Email {get;set;}
        [Required]
        [MinLength(8)]
        [DataType(DataType.Password)]
        public string Password {get;set;}
    }
}