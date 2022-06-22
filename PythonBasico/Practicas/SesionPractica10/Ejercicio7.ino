/*
 *Crear un programa para Ardunino que tenga 4 diodos led que son comandados por un pulsante. 
 *Cuando este se accione, las luces se encenderán aleatoriamente, i.e. el estado de cada diodo 
 *se calculará de forma aleatoria. Inicialmente las luces estarán todas apagadas.
*/


/*
 *URL DEL CIRCUITO: https://www.tinkercad.com/things/7bXSid9odT4
*/
//Constantes de circuitos asociados a puertos digitales
#define LED_AMARILLO 2
#define LED_AZUL 3
#define LED_VERDE 4
#define LED_ROJO 5
#define PULSADOR 6

void setup(){
    /*
    *Inicializa los componentes de circuito, se ejecuta una unica vez.
    */
    pinMode(LED_AMARILLO, OUTPUT);
    pinMode(LED_AZUL, OUTPUT);
    pinMode(LED_VERDE, OUTPUT);
    pinMode(LED_ROJO, OUTPUT);
    pinMode(PULSADOR, INPUT);
}

void loop()
{
    /*
    *Bloque principal de programa, se ejecuta indefinidamente, Ensiende y apaga 4 leds de 
    *manera aleatoria al presionar un pulsador.
    */
    //Verifica si se presiono el pulsante para ensender los leds.
    if(digitalRead(PULSADOR) == LOW){
        //Se asigna estados random a cada led.
        int estadosLeds [4] = {getEstadoRandom(), getEstadoRandom(), getEstadoRandom(), getEstadoRandom()};
        setEstadoLeds(estadosLeds);
        delay(1000);
    }else{
        int estadosLeds [4] = {LOW, LOW, LOW, LOW};
        setEstadoLeds(estadosLeds);
    }
}


void setEstadoLeds(int estados []){
    /*
    *Cambia el estado de los 4 led dependiendo la lista de estados recibida como parametro.
    * PARAMS
    * ------
    *   estados : int[]
    *       Lista con los estados de cada led, puede ser 1-HIGH o 0-LOW
    */
    digitalWrite(LED_AMARILLO, estados[0]);
    digitalWrite(LED_AZUL, estados[1]);
    digitalWrite(LED_VERDE, estados[2]);
    digitalWrite(LED_ROJO, estados[3]);
}


int getEstadoRandom(){
    /*
    *Genera un estado random que puede ser cero o uno.
    * RETURN
    * ------
    *   estado : int
    *       Número entero que puede ser uno o cero.
    */
    int numRandom = random(1,10);
    int estado = (numRandom > 5) ? HIGH : LOW;
    return estado;
}