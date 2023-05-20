/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Random;

/**
 *
 * @author Mauricio Di Donato Sánchez
 */
public class CrearCasos {
    private static final int NUM_TEST_CASES = 25;
    private static final int MIN_NUM_BOOKS = 2;
    private static final int MAX_NUM_BOOKS = 10;
    private static final int MAX_BOOK_PRICE = 100;
    private static final int MAX_PETER_MONEY = 100;
    
    public CrearCasos() throws IOException{
        rellenarArreglos();
    }
    
    public void rellenarArreglos() throws IOException {
        Random random = new Random();
        StringBuilder input = new StringBuilder();

        for (int i = 0; i < NUM_TEST_CASES; i++) {
            int numBooks = random.nextInt(MAX_NUM_BOOKS - MIN_NUM_BOOKS + 1) + MIN_NUM_BOOKS;
            int peterMoney = random.nextInt(MAX_PETER_MONEY) + 1;
            
            input.append(numBooks).append("\n");

            for (int j = 0; j < numBooks; j++) {
                int bookPrice = random.nextInt(peterMoney) + 1;
                input.append(bookPrice).append(" ");
            }
            input.append("\n");

            input.append(peterMoney).append("\n");

            input.append("\n");
        }

        String testCasesInput = input.toString();
        saveToFiles(testCasesInput);
    }
    
    public static void saveToFiles(String contentToWrite) throws IOException {
        String path = "./codigo/" + "input.txt";
        Files.write(Paths.get(path), contentToWrite.getBytes());
    }
    
}
