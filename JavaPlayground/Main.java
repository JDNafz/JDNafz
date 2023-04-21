class Main {
    public static void main(String[] args) {
        Library loringParkLibrary = new Library("loringParkLibrary");
        Library central = new Library("central");
        User user1 = new User("JD Naf","1992-01-24",loringParkLibrary);
        User user2 = new User("Elisabeth", "1999-03-13", central);

        Book rainbows = new Book("Rainbows on Fire","Kill Joy Frenkins",69, loringParkLibrary);
        AudioBook skysounds = new AudioBook("Skysounds","Skrillex", loringParkLibrary, 60 );
        
        EBook bandanas = new EBook("Bandanas","Tom Hanks",420, central, "mp3");
        
        
        user1.borrow(rainbows);
        user1.borrow(bandanas,central);
        user1.borrow(skysounds);
        // System.out.printf("user1's Books:\n%s \n", user1.getBooks())
        
        // Attempt to return book to wrong library
        // user1.returnBookTo(rainbows, central); 
        // user1.returnBookTo(rainbows, loringParkLibrary);

        // user2.borrow(skysounds);        
        // user2.borrow(rainbows, central);
        user2.borrow(rainbows, loringParkLibrary);

        // user1.getBooks();
        // user2.getBooks();

        
        // central.printAvailable();
        // user1.returnBookTo(rainbows, loringParkLibrary);
        // loringParkLibrary.printAvailable();


        // loringParkLibrary.printBooks();
        // central.printBooks();

    }
}