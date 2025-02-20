public class dorf extends stadt{

    String naechste_stadt;
    String fussballverein;

    public dorf(String name, int einwohnerzahl, double flaeche, double BIP, String buergermeister, String naechste_stadt, String fussballverein) 
    {
        super(name, einwohnerzahl, flaeche, BIP, buergermeister);
        this.naechste_stadt = naechste_stadt;
        this.fussballverein = fussballverein;
    }

    public String getNaechste_stadt() {
        return naechste_stadt;
    }
    public void setNaechste_stadt(String naechste_stadt) {
        this.naechste_stadt = naechste_stadt;
    }
    public String getFussballverein() {
        return fussballverein;
    }
    public void setFussballverein(String fussballverein) {
        this.fussballverein = fussballverein;
    }
}
