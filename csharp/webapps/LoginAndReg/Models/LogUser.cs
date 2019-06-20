using System;
using System.ComponentModel.DataAnnotations;

namespace LoginAndReg.Models
{
    public class LogUser
    {  
        [Required]
        [DataType(DataType.EmailAddress)]
        public string Email { get;set; }
        [Required]
        [DataType(DataType.Password)]
        [MinLength(8)]
        public string Password { get;set; }
    }
}