using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
using LostintheWoods.Models;
using Microsoft.Extensions.Options;
 
namespace LostintheWoods.Factory
{
    public class TrailFactory
    {
        public MySqlOptions _options;
        public TrailFactory(IOptions<MySqlOptions> config)
        {
            _options = config.Value;
        }
        internal IDbConnection Connection{
            get {
                return new MySqlConnection(_options.ConnectionString);
            }
        }

        public long AddNewTrail(Trail item){
            using (IDbConnection dbConnection = Connection)
            {
                string query = "INSERT INTO trails(TrailName, TrailDesc, TrailLength, ElevationChange, Longitude, Latitude) VALUES (@TrailName, @TrailDesc, @TrailLength, @ElevationChange, @Longitude, @Latitude)";
                dbConnection.Open();
                dbConnection.Execute(query, item);
                
                string idQuery = "SELECT * FROM trails ORDER BY id DESC LIMIT 1";
                Trail lastTrail = dbConnection.Query<Trail>(idQuery).LastOrDefault();
                return lastTrail.id;

            }
        }

        public List<Trail> ShowAllTrails(){
            using (IDbConnection dbConnection = Connection)
            {
                using(IDbCommand command = dbConnection.CreateCommand())
                {
                    string query = "SELECT * FROM trails";
                    dbConnection.Open();
                    return dbConnection.Query<Trail>(query).ToList();
                }
            }
        }

        public Trail ShowTrail(int trailID){
            using (IDbConnection dbConnection = Connection)
            {
                using(IDbCommand command = dbConnection.CreateCommand())
                {
                    string query = $"SELECT * FROM trails WHERE id = {trailID}";
                    dbConnection.Open();
                    return dbConnection.Query<Trail>(query).FirstOrDefault();
                }
            }            
        }

        public void DeleteTrail(int trailID){
            using (IDbConnection dbConnection = Connection)
            {
                using(IDbCommand command = dbConnection.CreateCommand())
                {
                    string query = $"DELETE FROM trails WHERE id = {trailID}";
                    dbConnection.Open();
                    dbConnection.Execute(query);
                }
            }
        }
    }
}