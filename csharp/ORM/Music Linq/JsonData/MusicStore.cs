using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class MusicStore
    {
        public List<Artist> AllArtists {get;set;}
        public List<Group> AllGroups {get;set;}
        public static MusicStore GetData()
        {
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            var ArtistsWithGroup = Artists.Join(Groups, 
                (a => a.GroupId), 
                (g => g.Id),
                (joinedA, joinedG) => {
                    joinedA.Group = joinedG;
                    return joinedA;
                })
                .Concat(Artists.Where(a => a.GroupId == 0))
                .ToList();

            var GroupsWithArtists = Groups.Join(Artists,
                (g => g.Id),
                (a => a.GroupId),
                (joinedG, joinedA) => {
                    joinedG.Members.Add(joinedA);
                    return joinedG;
                })
                .Distinct()
                .ToList();

            return new MusicStore()
            {
                AllArtists = ArtistsWithGroup,
                AllGroups = GroupsWithArtists
            };

        }
    }
}