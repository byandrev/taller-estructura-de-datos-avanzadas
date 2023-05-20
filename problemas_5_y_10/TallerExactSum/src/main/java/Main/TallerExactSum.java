/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package Main;
import Accesories.AutomatizarProceso;
import Modelo.CrearCasos;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @author Mauricio Di Donato Sánchez
 */
public class TallerExactSum {

    public static void main(String[] args) throws IOException {
        try {
            CrearCasos machine = new CrearCasos();
            AutomatizarProceso procesador = new AutomatizarProceso();
        } catch (InterruptedException ex) {
            Logger.getLogger(TallerExactSum.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
