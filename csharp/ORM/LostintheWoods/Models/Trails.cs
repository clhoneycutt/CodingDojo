using System;
using System.ComponentModel.DataAnnotations;

namespace LostintheWoods.Models
{
    public class Trail
    {
        [Key]
        public long id {get;set;}
        [Required]
        [MinLength(3)]
        public string TrailName {get;set;}
        [Required]
        [MinLength(15)]
        [DataType(DataType.MultilineText)]
        public string TrailDesc{get;set;}
        [Required]
        public float TrailLength{get;set;}
        [Required]
        public int ElevationChange{get;set;}
        [Required]
        public float Longitude{get;set;}
        [Required]
        public float Latitude{get;set;}
    }
}