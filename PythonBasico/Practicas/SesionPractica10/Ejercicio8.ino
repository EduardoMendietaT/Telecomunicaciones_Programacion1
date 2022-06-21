/*
 *Crear un porgrama para Arduino que muestre en la pantalla LCD el valor de lectura de un sensor de temperatura. 
 *También tendrá un pulsante; cuando este se accione, se mostrará en pantalla un valor numérico calculado a partir 
 *de un potenciómetro. Cuando el potenciómetro esté en su valor mínimo, se mostrará en la pantalla 0; y cuando 
 *esté en su valor máximo, se mostrará 100. Cuando se accione nuevamente el pulsante, se volverá a mostrar 
 *en pantalla la temperatura ambiente. ---------------------------------------------------------------------------
*/


/*
 *URL DEL CIRCUITO: https://www.tinkercad.com/things/eShPJAQu5D6
*/
#include <LiquidCrystal.h>

//Constantes de circuitos asociados a puertos digitales
#define TMP A0
#define POTENCIOMETRO A1
#define PULSADOR 8

//Contante con un valor de prueba para reiniciar las mediciones del sensor TMP y Potenciometro.
#define RESET -100

LiquidCrystal lcd(2, 3, 4, 5, 6, 7); //Inicia el objeto LCD

boolean cambioSalida = false; //Alterna entre los dos circuitos para obtener sus mediciones
int lectura = 0; //Lectura de valores tanto del Potenciometro y sensorTMP

//Asignamos un valor por defecto al otenciometro y sensorTMP
int valorActualPote = RESET;
int valorActualTMP = RESET;


void setup(){
    /*
    *Inicializa los componentes de circuito, se ejecuta una unica vez.
    */
    pinMode(PULSADOR, INPUT);
    lcd.begin(16, 2);
}


void loop(){ 
    /*
    *Bloque principal de programa, se ejecuta indefinidamente, imprime en una pantalla lcd, los valores
    *tomados de un potenciometro y un sensor de temperatura, alterna las salidas al presionar el pulsante.
    */
    //Valida cambio de salida al presionar el pulsante.
    if(digitalRead(PULSADOR) == LOW){
        delay(20);
        cambioSalida = !cambioSalida;
    }
    //cambia el circuito del cuál se toma las lecturas.
    if(!cambioSalida){
        lectura = getLecturaTMP();
        if(lectura != valorActualTMP){
            lcd.clear();
            valorActualTMP = lectura;
            lcd.print(String(valorActualTMP)+" grados C");//Imprime en la pantalla lcd.
            valorActualPote = RESET; //Resetea el valor del Potenciometro para que se muestre en pantalla.
        }
    }else{
        lectura = getLecturaPote();
        if(lectura != valorActualPote){
            lcd.clear();
            valorActualPote = lectura;
            lcd.print("Valor Pote: "+String(valorActualPote));
            valorActualTMP = RESET;
        }
    }
}


int getLecturaPote(){
    /*
     *Obtine la lectura actual del Potenciometro.
     *  RETURN
     *  ------
     *  medicion : int
     *      valor de medición.
     */
    int medicion = map(analogRead(POTENCIOMETRO), 0, 1023, 0, 100);
    return medicion;
}


int getLecturaTMP(){
    /*
     *Obtine la lectura actual del sensor de temperatura(TMP).
     *  RETURN
     *  ------
     *  medicion : int
     *      valor de medición.
     */
    int medicion = map(analogRead(TMP), 0, 1023, -50, 450);
	return medicion;
}