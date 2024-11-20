/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */



package Vista;

import java.awt.Color;
import java.awt.List;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.table.DefaultTableModel;
import org.json.JSONArray;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.swing.JOptionPane;
import org.json.Cookie;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author digim
 */
public class Usuarios extends javax.swing.JFrame {

    /**
     * Creates new form Menu
     */
    public Usuarios() {
        setResizable(false);
        initComponents();
        this.setLocationRelativeTo(null);
        
        Login login = new Login();
        txtUsuario.setText(login.TipoUsuario);
        

        
        
        
        cargarDatosTabla(); // Llamamos al método para cargar datos de la API en la tabla
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        BTEliminarUS = new javax.swing.JButton();
        txtUsuario = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        TableUsuarios = new javax.swing.JTable();
        BTSeleccionarUS = new javax.swing.JButton();
        BTVolver = new javax.swing.JButton();
        txtNombre = new javax.swing.JTextField();
        txtTelefono = new javax.swing.JTextField();
        txtRut = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        BTModificarUS1 = new javax.swing.JButton();
        txtEC = new javax.swing.JTextField();
        txtG = new javax.swing.JTextField();
        txtApellido = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        txtEmail = new javax.swing.JTextField();
        jLabel8 = new javax.swing.JLabel();
        txtUsername = new javax.swing.JTextField();
        jLabel9 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(51, 204, 255));

        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        jLabel1.setText("Bienvenido:");

        BTEliminarUS.setText("Eliminar Usuarios");
        BTEliminarUS.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTEliminarUSActionPerformed(evt);
            }
        });

        txtUsuario.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        txtUsuario.setText("@NOMBRE ADMIN");

        TableUsuarios.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null, null},
                {null, null, null, null, null, null},
                {null, null, null, null, null, null},
                {null, null, null, null, null, null}
            },
            new String [] {
                "ID", "Usuario", "Rut", "Telefono", "Estado Economico", "Genero"
            }
        ));
        jScrollPane2.setViewportView(TableUsuarios);

        BTSeleccionarUS.setText("Seleccionar Usuario");
        BTSeleccionarUS.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTSeleccionarUSActionPerformed(evt);
            }
        });

        BTVolver.setText("Volver");
        BTVolver.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTVolverActionPerformed(evt);
            }
        });

        txtNombre.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtNombreActionPerformed(evt);
            }
        });

        jLabel2.setText("Nombre");

        jLabel3.setText("Rut");

        jLabel4.setText("Telefono");

        jLabel5.setText("Estado Economico");

        jLabel6.setText("Genero");

        BTModificarUS1.setText("Modificar Usuarios");
        BTModificarUS1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTModificarUS1ActionPerformed(evt);
            }
        });

        txtApellido.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtApellidoActionPerformed(evt);
            }
        });

        jLabel7.setText("Apellido");

        txtEmail.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtEmailActionPerformed(evt);
            }
        });

        jLabel8.setText("Nombre de Usuario");

        txtUsername.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtUsernameActionPerformed(evt);
            }
        });

        jLabel9.setText("Email");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addComponent(BTVolver)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel1)
                        .addGap(46, 46, 46)
                        .addComponent(txtUsuario)
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(55, 55, 55)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(jPanel1Layout.createSequentialGroup()
                                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(jLabel2)
                                            .addComponent(jLabel7)
                                            .addComponent(jLabel8))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 57, Short.MAX_VALUE)
                                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(txtApellido, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(txtUsername, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                    .addGroup(jPanel1Layout.createSequentialGroup()
                                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(jLabel3)
                                            .addComponent(jLabel4)
                                            .addComponent(jLabel5)
                                            .addComponent(jLabel6))
                                        .addGap(62, 62, 62)
                                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(txtEC, javax.swing.GroupLayout.Alignment.TRAILING)
                                            .addComponent(txtTelefono, javax.swing.GroupLayout.Alignment.TRAILING)
                                            .addComponent(txtRut)
                                            .addComponent(txtG)))
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                        .addComponent(jLabel9)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(txtEmail, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                .addGap(52, 52, 52))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addGap(0, 0, Short.MAX_VALUE)
                                .addComponent(BTSeleccionarUS)
                                .addGap(130, 130, 130))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(72, 72, 72)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(BTEliminarUS, javax.swing.GroupLayout.PREFERRED_SIZE, 250, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(BTModificarUS1, javax.swing.GroupLayout.PREFERRED_SIZE, 250, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                        .addComponent(jScrollPane2, javax.swing.GroupLayout.DEFAULT_SIZE, 608, Short.MAX_VALUE)))
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(10, 10, 10)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtUsuario)
                            .addComponent(jLabel1)))
                    .addComponent(BTVolver))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane2)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(BTSeleccionarUS)
                        .addGap(13, 13, 13)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel2)
                            .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(14, 14, 14)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtApellido, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel7))
                        .addGap(26, 26, 26)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel8)
                            .addComponent(txtUsername, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel9))
                        .addGap(21, 21, 21)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtRut, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel3))
                        .addGap(17, 17, 17)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtTelefono, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel4))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel5)
                            .addComponent(txtEC, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel6)
                            .addComponent(txtG, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addComponent(BTModificarUS1, javax.swing.GroupLayout.PREFERRED_SIZE, 79, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(35, 35, 35)
                        .addComponent(BTEliminarUS, javax.swing.GroupLayout.PREFERRED_SIZE, 79, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 136, Short.MAX_VALUE)))
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void BTVolverActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTVolverActionPerformed
            Menu_Admin Menu_a = new Menu_Admin();
            Menu_a.setVisible(true);
            this.dispose();
    }//GEN-LAST:event_BTVolverActionPerformed

    private void txtNombreActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtNombreActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtNombreActionPerformed

    private void BTSeleccionarUSActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTSeleccionarUSActionPerformed
        manejarSeleccionUsuario(); // Llama al método para manejar la selección del usuario
    }//GEN-LAST:event_BTSeleccionarUSActionPerformed

    private void BTEliminarUSActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTEliminarUSActionPerformed
        manejarEliminacionUsuario();
    }//GEN-LAST:event_BTEliminarUSActionPerformed

    private void BTModificarUS1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTModificarUS1ActionPerformed

    }//GEN-LAST:event_BTModificarUS1ActionPerformed

    private void txtApellidoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtApellidoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtApellidoActionPerformed

    private void txtEmailActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtEmailActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtEmailActionPerformed

    private void txtUsernameActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtUsernameActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtUsernameActionPerformed

private int usuarioId; // Variable para almacenar la ID seleccionada
private String token = "b0533e8356de17655c128d5fa9a6ca4a0537872d";

public void inicializarComponentes() {

    
    // Cargar los datos en la tabla
    cargarDatosTabla(); // Llama al método para cargar los datos al inicio
}
    // Método para obtener el token CSRF desde la API (suponiendo que se obtiene de alguna cookie)
    private String obtenerTokenCSRFDesdeAPI() {
        // Este método debe devolver el token CSRF desde las cookies o encabezado
        // Aquí puedes escribir código que obtenga el token desde una cookie, por ejemplo:
        // String cookieHeader = connection.getHeaderField("Set-Cookie");
        return "http://127.0.0.1:8000/api/"; // Este es solo un valor ejemplo
    }

    // Obtener las cookies desde la respuesta (si estás usando HttpURLConnection)
    private String getCookieFromResponse(HttpURLConnection connection) {
        String cookieHeader = connection.getHeaderField("Set-Cookie");
        if (cookieHeader != null) {
            String[] cookies = cookieHeader.split(";");
            for (String cookie : cookies) {
                if (cookie.contains("csrftoken")) {
                    return cookie.split("=")[1];  // Extrae el valor del token
                }
            }
        }
        return null;
    }

//--------------------------------------------------------INICIO LISTAR DATOS-------------------------------------------------------------------------
    private void cargarDatosTabla() {
    String urlString = "http://127.0.0.1:8000/api/perfilusuario/?format=json";
    DefaultTableModel model = (DefaultTableModel) TableUsuarios.getModel();
    model.setRowCount(0); // Limpiar la tabla antes de cargar nuevos datos

    try {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Token " + token);
        connection.connect();

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String inputLine;

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            // Parsear JSON
            JSONArray usuariosArray = new JSONArray(response.toString());
            for (int i = 0; i < usuariosArray.length(); i++) {
                JSONObject usuarioObj = usuariosArray.getJSONObject(i);

                // Obtener la ID y otros atributos
                int id = usuarioObj.getInt("id");
                String rut = usuarioObj.optString("rut", "N/A");
                String telefono = usuarioObj.optString("telefono", "N/A");

                // Procesar estado económico como objeto JSON
                JSONObject estadoEconomicoObj = usuarioObj.optJSONObject("estado_economico");
                String estadoEconomico = "N/A";
                if (estadoEconomicoObj != null) {
                    estadoEconomico = estadoEconomicoObj.optString("descripcion", "N/A");
                }

                // Procesar genero como objeto JSON o cadena simple
                String genero = "N/A";
                JSONObject generoObj = usuarioObj.optJSONObject("genero");
                if (generoObj != null) {
                    genero = generoObj.optString("descripcion", "N/A");
                } else {
                    // Si genero es un valor simple, asignarlo directamente
                    genero = usuarioObj.optString("genero", "N/A");
                }

                // Obtener el objeto dentro de "usuario_django"
                JSONObject usuarioDjango = usuarioObj.optJSONObject("usuario_django");

                if (usuarioDjango != null) {
                    String lastName = usuarioDjango.optString("last_name", "N/A");
                    String firstName = usuarioDjango.optString("first_name", "N/A");
                    String email = usuarioDjango.optString("email", "N/A");

                    System.out.println("Apellido: " + lastName);
                    System.out.println("Nombre: " + firstName);
                    System.out.println("Email: " + email);
                    System.out.println("Estado Económico: " + estadoEconomico);
                    System.out.println("Género: " + genero);
                    

                    // Añadir los datos a la tabla
                    model.addRow(new Object[]{id, firstName, lastName, rut, telefono, estadoEconomico, genero});
                } else {
                    System.out.println("El campo 'usuario_django' no contiene un objeto JSON válido.");
                }
            }
        } else {
            JOptionPane.showMessageDialog(this, "Error en la conexión. Código de respuesta: " + responseCode);
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(this, "Error al cargar datos de la API.");
    }
}


//-------------------------------------------------------FIN LISTAR DATOS---------------------------------------------------------------------
    
    
//-------------------------------------------------------INICIO MODIFICAR------------------------------------------------//


 
//-----------------------------------------------------FIN MODIFICAR------------------------------------------------------------------------
    
//-----------------------------------------------------INICIO ELIMINAR----------------------------------------------------------------------
    
    // Método para eliminar un usuario a través de la API
    private void eliminarUsuario(int usuarioId) {
        String urlString = "http://127.0.0.1:8000/api/perfilusuario/" + usuarioId + "/"; // URL de la API para eliminar

        try {
            // Crear la URL y la conexión
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Configurar el método DELETE y los encabezados
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Token " + token);  // Token de autenticación
            connection.setRequestProperty("Accept", "application/json");

            // Conectar y obtener la respuesta
            connection.connect();
            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_NO_CONTENT) {
                JOptionPane.showMessageDialog(null, "Usuario eliminado correctamente.");
                // Aquí puedes actualizar la tabla o hacer otras acciones
            } else {
                JOptionPane.showMessageDialog(null, "Error al eliminar usuario. Código de respuesta: " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(null, "Error al eliminar usuario.");
        }
    }

    // Método común para manejar la eliminación del usuario
    private void manejarEliminacionUsuario() {
        // Obtener la fila seleccionada
        int filaSeleccionada = TableUsuarios.getSelectedRow();

        if (filaSeleccionada != -1) {
            // Obtener el ID del usuario en la primera columna (suponiendo que el ID está en la columna 0)
            int usuarioId = (int) TableUsuarios.getValueAt(filaSeleccionada, 0);

            // Mostrar un cuadro de confirmación para eliminar el usuario
            int confirmacion = JOptionPane.showConfirmDialog(null, 
                "¿Está seguro de que desea eliminar este usuario?", 
                "Confirmar eliminación", 
                JOptionPane.YES_NO_OPTION);

            if (confirmacion == JOptionPane.YES_OPTION) {
                eliminarUsuario(usuarioId); // Llamar al método de eliminación
                cargarDatosTabla();
            }
        } else {
            JOptionPane.showMessageDialog(null, "Por favor, seleccione un usuario de la tabla.");
        }
    }

    // Método para agregar el listener al hacer clic en la fila de la tabla
    private void agregarListenerTabla() {
        TableUsuarios.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                manejarEliminacionUsuario(); // Llamar al método común
            }
        });
    }

    
//-----------------------------------------------------FIN ELIMINAR-------------------------------------------------------------------------

    
//-----------------------------------------------------INICIO SELECCIONAR USUARIO-----------------------------------------------------------
    
// Método para seleccionar un usuario y cargar sus datos desde la API
// Método para cargar los datos del usuario seleccionado
private void seleccionarUsuario(int usuarioId) {
    String urlString = "http://127.0.0.1:8000/api/perfilusuario/" + usuarioId + "/"; // URL de la API para obtener datos

    try {
        // Crear la URL y la conexión
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Configurar el método GET y los encabezados
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Token " + token);  // Token de autenticación
        connection.setRequestProperty("Accept", "application/json");

        // Conectar y obtener la respuesta
        connection.connect();
        int responseCode = connection.getResponseCode();

        if (responseCode == HttpURLConnection.HTTP_OK) {
            // Leer la respuesta de la API
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            // Convertir la respuesta en un JSONObject
            JSONObject jsonResponse = new JSONObject(response.toString());

            // Procesar estado económico como objeto JSON
            String estadoEconomico = "N/A";
            JSONObject estadoEconomicoObj = jsonResponse.optJSONObject("estado_economico");
            if (estadoEconomicoObj != null) {
                estadoEconomico = estadoEconomicoObj.optString("descripcion", "N/A");
            }

            // Procesar genero como objeto JSON o cadena simple
            String genero = "N/A";
            JSONObject generoObj = jsonResponse.optJSONObject("genero");
            if (generoObj != null) {
                genero = generoObj.optString("descripcion", "N/A");
            } else {
                // Si genero es un valor simple, asignarlo directamente
                genero = jsonResponse.optString("genero", "N/A");
            }

            // Obtener los datos de usuario_django (que es un diccionario)
            String firstName = "N/A";
            String lastName = "N/A";
            String username = "N/A";
            String email = "N/A";
            if (jsonResponse.has("usuario_django")) {
                JSONObject usuarioDjango = jsonResponse.getJSONObject("usuario_django");
                firstName = usuarioDjango.optString("first_name", "N/A");
                lastName = usuarioDjango.optString("last_name", "N/A");
                username = usuarioDjango.optString("username", "N/A");
                email = usuarioDjango.optString("email", "N/A");
            }

            // Obtener otros datos del usuario
            String rut = jsonResponse.optString("rut", "N/A");
            String telefono = jsonResponse.optString("telefono", "N/A");

            // Mostrar los datos en los campos correspondientes
            txtNombre.setText(firstName);
            txtApellido.setText(lastName);
            txtRut.setText(rut);
            txtTelefono.setText(telefono);
            txtUsername.setText(username);  // Asumiendo que tienes un campo para mostrar el username
            txtEmail.setText(email);  // Asumiendo que tienes un campo para mostrar el email

            // Mostrar valores procesados para estado económico y genero
            txtEC.setText(estadoEconomico);
            txtG.setText(genero);

            // Deshabilitar los campos que no deben ser modificados
            txtNombre.setEditable(false);
            txtNombre.setBackground(Color.GRAY);

            txtApellido.setEditable(false);
            txtApellido.setBackground(Color.GRAY);

            txtRut.setEditable(false);
            txtRut.setBackground(Color.GRAY);

            txtG.setEditable(false);
            txtG.setBackground(Color.GRAY);

        } else {
            JOptionPane.showMessageDialog(null, "Error al obtener datos del usuario.");
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al seleccionar usuario.");
    }
}


// Método para manejar la selección del usuario en la tabla y cargar datos
private void manejarSeleccionUsuario() {
    // Obtener la fila seleccionada
    int filaSeleccionada = TableUsuarios.getSelectedRow();

    if (filaSeleccionada != -1) {
        // Obtener el ID del usuario en la primera columna (suponiendo que el ID está en la columna 0)
        int usuarioId = (int) TableUsuarios.getValueAt(filaSeleccionada, 0);

        // Confirmación de selección
        int confirmacion = JOptionPane.showConfirmDialog(null,
            "¿Está seguro de que desea cargar los datos de este usuario?",
            "Confirmar selección",
            JOptionPane.YES_NO_OPTION);

        if (confirmacion == JOptionPane.YES_OPTION) {
            seleccionarUsuario(usuarioId); // Llamar al método para cargar los datos
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione un usuario de la tabla.");
    }
}






    
        


   
//-----------------------------------------------------FIN SELECCIONAR USUARIO--------------------------------------------------------------


    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Usuarios.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Usuarios().setVisible(true);
            }
        });
    }
    

    

        
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BTEliminarUS;
    private javax.swing.JButton BTModificarUS1;
    private javax.swing.JButton BTSeleccionarUS;
    private javax.swing.JButton BTVolver;
    private javax.swing.JTable TableUsuarios;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTextField txtApellido;
    private javax.swing.JTextField txtEC;
    private javax.swing.JTextField txtEmail;
    private javax.swing.JTextField txtG;
    private javax.swing.JTextField txtNombre;
    private javax.swing.JTextField txtRut;
    private javax.swing.JTextField txtTelefono;
    private javax.swing.JTextField txtUsername;
    private javax.swing.JLabel txtUsuario;
    // End of variables declaration//GEN-END:variables


}
