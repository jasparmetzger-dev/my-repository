public class Main {

    public static void main(String[] args) {

        hauptstadt berlin = new hauptstadt(
            "Berlin", 
            3_669_491,
            891.8, 
            193,
            "Kai Wegner",  
            "Deutschland",   
            "Parlamentarische Demokratie" 
        );

        stadt dresden = new stadt("Dreden",
        560_000,
        328.8,
        22,
        "Dirk Hilbert");

        hauptstadt paris = new hauptstadt("Paris",
         2_170_000,
        105.4,
        783,
        "Anne Hidalgo",
        "Frankreich",
        "Parlamentarische Demokratie");


        dorf haibach = new dorf("Haibach",
         0, 0, 0, null, null, null);

        //print alles mögliche (bis jz nur berlin)

        System.out.println("Stadtname: " + berlin.getName());
        System.out.println("Einwohnerzahl: " + berlin.getEinwohnerzahl());
        System.out.println("Fläche: " + berlin.getFlaeche() + " km²");
        System.out.println("BIP: " + berlin.getBIP() + " Milliarden Euro");
        System.out.println("Bürgermeister: " + berlin.getBuergermeister());
        System.out.println("Land: " + berlin.getLand());
        System.out.println("Regierungsform: " + berlin.getRegierungsformLand());
        System.out.println("Bevölkerungsdichte: " + berlin.getBevoelkerungsdichte() + " Einwohner/km²");
    }
}

