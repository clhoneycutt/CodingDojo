namespace phones
{
    public class Galaxy : Phone, IRingable 
    {
        public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
            : base(versionNumber, batteryPercentage, carrier, ringTone) {}

        public string Ring() 
        {
            // your code here
        }
                    
        public string Unlock() 
        {
            // your code here
        }
        public override void DisplayInfo() 
        {
            // your code here            
        }
    }
}