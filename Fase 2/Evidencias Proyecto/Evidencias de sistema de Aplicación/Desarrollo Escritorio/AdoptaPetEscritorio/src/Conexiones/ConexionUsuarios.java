/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URL;
import org.json.JSONArray;
import org.json.JSONObject;
/**
 *
 * @author digim
 */
public class ConexionUsuarios {
    

public static void main(String[] args) {
        // URL de la API a la que quieres hacer la solicitud
        String urlString = "http://127.0.0.1:8000/api/perfilusuario/?format=json";

        // Token de autenticación (reemplázalo con tu token real)
        String token = "3469a77e70d09db05445ce3b6b4ff0316dcc1f29";

        try {
            // Crear el objeto URL
            URL url = new URL(urlString);

            // Abrir la conexión HTTP
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Establecer el método HTTP (GET, POST, etc.)
            connection.setRequestMethod("GET");

            // Establecer el encabezado Authorization con el token
            connection.setRequestProperty("Authorization", "Token " + token);

            // Conectar a la API
            connection.connect();

            // Comprobar el código de respuesta
            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) { // Código 200
                // Leer la respuesta de la API
                BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String inputLine;
                StringBuilder response = new StringBuilder();

                while ((inputLine = in.readLine()) != null) {
                    response.append(inputLine);
                }
                in.close();

                // Imprimir la respuesta de la API
                System.out.println("Respuesta de la API: " + response.toString());
            } else {
                // Si la respuesta no fue 200, mostrar el error
                System.out.println("Error en la conexión. Código de respuesta: " + responseCode);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }



}


    

