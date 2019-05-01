using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = MusicStore.GetData().AllArtists;
            List<Group> Groups = MusicStore.GetData().AllGroups;

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?

            Artist mtVernonArtist = Artists.FirstOrDefault(a => a.Hometown == "Mount Vernon");
            Console.WriteLine($"The only artist from Mt Vernon is {mtVernonArtist.ArtistName} (Age: {mtVernonArtist.Age}), who was born as {mtVernonArtist.RealName}.");
            

            //Who is the youngest artist in our collection of artists?

            Artist youngestArtist = Artists.FirstOrDefault(a => a.Age == Artists.Min(age => age.Age));
            Console.WriteLine($"The youngest artist is {youngestArtist.ArtistName} (Age: {youngestArtist.Age}).  Born as {youngestArtist.RealName}.");

            //Display all artists with 'William' somewhere in their real name

            IEnumerable<Artist> Williams = Artists.Where(a => a.RealName.Contains("William")).ToList();
            Console.WriteLine("The following artists all have William somewhere in their name");
            foreach(Artist artist in Williams)
            {
                Console.WriteLine($"Name: {artist.ArtistName} Real Name: {artist.RealName} ");
            }

            
            //Display the 3 oldest artist from Atlanta

            IEnumerable<Artist> topThreeOldest = Artists
                .Where(a => a.Hometown == "Atlanta")
                .OrderByDescending(a => a.Age)
                .Take(3);
            Console.WriteLine("The following are the 3 oldest artists from Atlanta");
            foreach(Artist artist in topThreeOldest)
            {
                Console.WriteLine($"Name: {artist.ArtistName} Real Name: {artist.RealName}");
            }

            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
	        Console.WriteLine(Groups.Count);
        }
    }
}
