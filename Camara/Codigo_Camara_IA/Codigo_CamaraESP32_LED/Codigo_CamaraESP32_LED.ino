#include "esp_camera.h"

#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>

#include <HTTPClient.h>

#include <WebServer.h>

#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"
 
#define LedVerde 12
#define LedRojo 13

// Casa
// const char* ssid = "IZZI-557E"; // Nombre de la red WiFi
// const char* password = "fMfKAEGF"; // Contraseña de la red WiFi
//String URL = "http://192.168.1.4:5074/Sensores";

// TEC
const char* ssid = "Tec-IoT";
const char* password = "spotless.magnetic.bridge";
String URL = "http://10.22.225.125:5074/Sensores";

// Inicialización de servidor web en el puerto 80 y configuración del DHT
WebServer server(80);

// Las variables del servidor
HTTPClient httpClient;
WiFiClient wClient;

// Las variables para los registros:
// Variable booleana para la deteccion de rostro
bool deteccionRostro = false;
long milisegundos = 0;
int intervalo = 10000;

// Se llama la funcion que inicializa  la cámara
void startCameraServer();

void setup() {

  // Se declara que se usara los leds
  pinMode(LedVerde,OUTPUT);
  pinMode(LedRojo,OUTPUT);

  digitalWrite(LedRojo,HIGH);
  digitalWrite(LedVerde,LOW);

  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();


  // La configuracion de la cámara
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  config.frame_size = FRAMESIZE_CIF;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  // Se inicializa de la cámara
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("La inicialización de la cámara falló con error 0x%x", err);
    return;
  }

  // La conexion a Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi conectado");

  // Se inicia servidor de cámara
  startCameraServer();

  // Se configura servidor web
  Serial.print("Cámara lista! Utiliza 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' para conectar");

}

void loop() {
  unsigned long tiempoActual = millis();

  // Si detecta una cara guardada prende el led
  if (deteccionRostro == true) {
    digitalWrite(LedVerde, HIGH);
    digitalWrite(LedRojo, LOW);
    logAPI(7);
    milisegundos=millis();
  } 
  // Si no, prende el led rojo
  if(millis() - milisegundos > intervalo && deteccionRostro == false) {
    digitalWrite(LedVerde, LOW);
    digitalWrite(LedRojo, HIGH);
    logAPI(8);
  }
}

// Las variables para la informacion
int id_registro = 1;  // Valor inicial
const int id_empleado = 2; // Lo dejamos constante
const int id_accesoZona = 3; // 3 porque es boveda

void logAPI(int id_tipoSensor) {
  if (WiFi.status() == WL_CONNECTED) {

    // La información a mandar
    String postData = "{\"id_registro\":" + String(id_registro) +
                      ",\"id_empleado\":" + String(id_empleado) +
                      ",\"id_tipoSensor\":" + String(id_tipoSensor) +
                      ",\"id_accesoZona\":" + String(id_accesoZona) +
                      ",\"fecha\":\"2024-11-02\"}";

    id_registro++;  // Se incrementa el ID de registro

    // Se confirma el envío de la información
    Serial.print("Se envió la información: ");
    Serial.println(postData);

    // Un delay para que la persona reposicione su cara
    delay(30000);
    
    // Se envia la informacion al API
    httpClient.begin(wClient, URL);
    httpClient.addHeader("Content-Type", "application/json");

    // Enviar el POST request
    int httpCode = httpClient.POST(postData);

    // Nos da el codigo de respuesta
    Serial.print("Código de respuesta: ");
    Serial.println(httpCode);

    httpClient.end();
  }
}

// Me baso en esta funcion para enviar la informacion

// void logIntento(float t){
//   if(WiFi.status() == WL_CONNECTED){

//     String device = "1";
//     String temp;
//     temp= String(t);
//     String postData;
//     postData = "{\"idRegistro\":0,\"idTipoSensor\":"+device+", \"valor\":"+temp+", \"logDate\":\"2024-10-23\"}";
//     Serial.print("Post Data String: ");
//     Serial.println(postData);
    
//     Serial.print("Host: ");
//     Serial.println(URL);

//     httpClient.begin(wClient, URL);
//     httpClient.addHeader("Content-Type", "application/json");

//     int httpCode = httpClient.POST(postData);

//     Serial.print("Response Code: ");
//     Serial.println(httpCode);

//     httpClient.end(); 
//   }
//   return;
// }