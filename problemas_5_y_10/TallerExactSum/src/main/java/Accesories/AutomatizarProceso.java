/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Accesories;

import java.io.File;
import java.io.IOException;

/**
 *
 * @author Mauricio Di Donato Sánchez
 */
public class AutomatizarProceso {
    public AutomatizarProceso() throws IOException, InterruptedException{
        AutomatizarYProcesar();
    }
    
    public void AutomatizarYProcesar() throws IOException, InterruptedException {

        // Compilar el archivo codigo.cpp
        ProcessBuilder compileProcessBuilder = new ProcessBuilder("c++", "./codigo/solution.cpp", "-o", "./codigo/problem.exe");
        Process compileProcess = compileProcessBuilder.start();
        compileProcess.waitFor();
        
        //Ejecutar casos
        
        ProcessBuilder executeProcessBuilder = new ProcessBuilder("./codigo/problem.exe");
            executeProcessBuilder.redirectInput(new File("./codigo/input.txt"));
            executeProcessBuilder.redirectOutput(new File("./codigo/output.txt"));
            Process executeProcess = executeProcessBuilder.start();
            executeProcess.waitFor();
    }
}
