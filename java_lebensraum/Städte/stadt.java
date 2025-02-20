package Städte;
public class stadt 
{
    private String name;
    private int einwohnerzahl;
    private double flaeche;
    private double BIP;
    private String buergermeister;

    public stadt(String name, int einwohnerzahl, double flaeche, double BIP, String buergermeister)
    {
        this.name = name;
        this.einwohnerzahl = einwohnerzahl;
        this.flaeche = flaeche;
        this.BIP = BIP;
        this.buergermeister = buergermeister;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getEinwohnerzahl() {
        return einwohnerzahl;
    }
    public void setEinwohnerzahl(int einwohnerzahl) {
        this.einwohnerzahl = einwohnerzahl;
    }
    public double getFlaeche() {
        return flaeche;
    }
    public void setFlaeche(double flaeche) {
        this.flaeche = flaeche;
    }
    public double getBIP() {
        return BIP;
    }
    public void setBIP(double BIP) {
        this.BIP = BIP;
    }
    public String getBuergermeister() {
        return buergermeister;
    }
    public void setBuergermeister(String buergermeister) {
        this.buergermeister = buergermeister;
    }


    public double getBevoelkerungsdichte()
    {
        return einwohnerzahl / flaeche;
    }
}