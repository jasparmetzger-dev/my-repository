package Städte;

public class hauptstadt extends stadt
{
    String land;
    String regierungsform_land;

    public hauptstadt(String name, int einwohnerzahl, double flaeche, double BIP, String buergermeister, String land, String regierungsform_land) 
    {
        super(name, einwohnerzahl, flaeche, BIP, buergermeister);
        this.land = land;
        this.regierungsform_land = regierungsform_land;
    }
    
    public String getLand() {
        return land;
    }
    public void setLand(String land) {
        this.land = land;
    }
    public String getRegierungsformLand() {
        return regierungsform_land;
    }
    public void setRegierungsformLand(String regierungsform_land) {
        this.regierungsform_land = regierungsform_land;
    }
}
