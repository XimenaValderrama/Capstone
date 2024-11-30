/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package Vista;

import java.awt.Image;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableModel;
import javax.xml.ws.Response;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 *
 * @author digim
 */
public class Fundaciones extends javax.swing.JFrame {


    public Fundaciones() {
        setTitle("GESTIONAR FUNDACIONES");
        setResizable(false);
        initComponents();
        this.setLocationRelativeTo(null);
        
        Login login = new Login();
        txtUsuario.setText(login.TipoUsuario);
        cargarDatosTabla(); // Llamamos al método para cargar datos de la API en la tabla
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setIconImage(new ImageIcon("src/Img/Icono.png").getImage());
       
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        BTEliminarP = new javax.swing.JButton();
        txtUsuario = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        TablaFundaciones = new javax.swing.JTable();
        BTModificarP = new javax.swing.JButton();
        BTVolver = new javax.swing.JButton();
        BTAgregarF = new javax.swing.JButton();
        txtNombre = new javax.swing.JTextField();
        txtDescrip = new javax.swing.JTextField();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        BTSeleccionarI = new javax.swing.JButton();
        txtImagenUrl = new javax.swing.JTextField();
        jLabel4 = new javax.swing.JLabel();
        txtURLFunda = new javax.swing.JTextField();
        BTSeleccionarFund = new javax.swing.JButton();
        jLabel8 = new javax.swing.JLabel();

        jLabel6.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Img/logo.png"))); // NOI18N

        jLabel7.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Img/logo.png"))); // NOI18N

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(94, 114, 228));

        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        jLabel1.setText("Bienvenido:");

        BTEliminarP.setText("Eliminar Fundacion");
        BTEliminarP.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTEliminarPActionPerformed(evt);
            }
        });

        txtUsuario.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        txtUsuario.setText("@NOMBRE ADMIN o Usuario");

        TablaFundaciones.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "ID", "Nombre", "Descripcion Fundacion", "Imagen", "Url Fundacion"
            }
        ));
        jScrollPane2.setViewportView(TablaFundaciones);
        if (TablaFundaciones.getColumnModel().getColumnCount() > 0) {
            TablaFundaciones.getColumnModel().getColumn(2).setMinWidth(120);
        }

        BTModificarP.setText("Modificar Fundacion");
        BTModificarP.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTModificarPActionPerformed(evt);
            }
        });

        BTVolver.setText("Volver");
        BTVolver.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTVolverActionPerformed(evt);
            }
        });

        BTAgregarF.setText("Agregar Fundacion");
        BTAgregarF.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTAgregarFActionPerformed(evt);
            }
        });

        jLabel2.setText("Nombre");

        jLabel3.setText("Descripcion de la Fundacion");

        jLabel5.setText("Url Fundacion");

        BTSeleccionarI.setText("Seleccionar Imagen");
        BTSeleccionarI.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTSeleccionarIActionPerformed(evt);
            }
        });

        jLabel4.setText("Imagen");

        BTSeleccionarFund.setText("Seleccionar Fundacion");
        BTSeleccionarFund.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTSeleccionarFundActionPerformed(evt);
            }
        });

        jLabel8.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Img/logo.png"))); // NOI18N

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addComponent(BTVolver)
                .addGap(75, 75, 75)
                .addComponent(jLabel1)
                .addGap(47, 47, 47)
                .addComponent(txtUsuario)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(128, 128, 128)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(BTAgregarF, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 233, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(BTModificarP, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 233, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(BTEliminarP, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 233, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jLabel8, javax.swing.GroupLayout.PREFERRED_SIZE, 106, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel2)
                                    .addComponent(jLabel4)
                                    .addComponent(jLabel5))
                                .addGap(143, 143, 143)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(txtURLFunda)
                                    .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                        .addComponent(txtDescrip)
                                        .addComponent(BTSeleccionarI, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(txtImagenUrl)
                                        .addGroup(jPanel1Layout.createSequentialGroup()
                                            .addComponent(txtNombre)
                                            .addGap(4, 4, 4)))))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel3)
                                .addGap(0, 0, Short.MAX_VALUE))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(BTSeleccionarFund)
                                .addGap(85, 85, 85)))))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 775, javax.swing.GroupLayout.PREFERRED_SIZE))
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
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(BTVolver)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel8, javax.swing.GroupLayout.PREFERRED_SIZE, 80, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(BTSeleccionarFund)
                        .addGap(12, 12, 12)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel2))
                        .addGap(31, 31, 31)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel3)
                            .addComponent(txtDescrip, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(BTSeleccionarI)
                            .addComponent(jLabel4))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txtImagenUrl, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(29, 29, 29)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel5)
                            .addComponent(txtURLFunda, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(19, 19, 19)
                        .addComponent(BTAgregarF, javax.swing.GroupLayout.PREFERRED_SIZE, 70, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(BTModificarP, javax.swing.GroupLayout.PREFERRED_SIZE, 70, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(BTEliminarP, javax.swing.GroupLayout.PREFERRED_SIZE, 70, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(20, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
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

    private void BTEliminarPActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTEliminarPActionPerformed
        manejarEliminacionFundacion();
    }//GEN-LAST:event_BTEliminarPActionPerformed

    private void BTAgregarFActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTAgregarFActionPerformed
        agregarFundacion();
    }//GEN-LAST:event_BTAgregarFActionPerformed

    private void BTSeleccionarIActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTSeleccionarIActionPerformed
        seleccionarImagen();
    }//GEN-LAST:event_BTSeleccionarIActionPerformed

    private void BTSeleccionarFundActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTSeleccionarFundActionPerformed
        manejarSeleccionFundacion(); // Llama al método para manejar la selección del usuario
    }//GEN-LAST:event_BTSeleccionarFundActionPerformed

    private void BTModificarPActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTModificarPActionPerformed
        manejarModificacionFundacion();
    }//GEN-LAST:event_BTModificarPActionPerformed

    
private String token = "8ffeb3f8e3edc9915795f7c57fb11b39b1dd96a2";
private String token2 = "a635c77de3de8cf58fa3e631b4e197b048670150";


//------------------------------------------INICIO LISTAR FUNDACIONES-------------------------------------------------------------------------
private void cargarDatosTabla() {
    String fundacionesUrl = "http://127.0.0.1:8000/api/fundacion/?format=json"; // URL de las fundaciones
    DefaultTableModel model = (DefaultTableModel) TablaFundaciones.getModel();
    model.setRowCount(0); // Limpiar la tabla antes de cargar nuevos datos

    try {
        // Obtener datos de las fundaciones
        JSONArray fundacionesArray = obtenerDatosDeApi(fundacionesUrl);

        // Procesar datos de las fundaciones
        for (int i = 0; i < fundacionesArray.length(); i++) {
            JSONObject fundacionObj = fundacionesArray.getJSONObject(i);

            // Obtener los datos necesarios para la tabla
            int id = fundacionObj.optInt("id", -1);
            String nombre = fundacionObj.optString("nombre", "N/A");
            String descFundacion = fundacionObj.optString("desc_fundacion", "N/A");
            String imagen = fundacionObj.optString("imagen", "N/A");
            String urlFundacion = fundacionObj.optString("url_fundacion", "N/A");


            // Añadir datos a la tabla
            model.addRow(new Object[]{id, nombre, descFundacion, imagen, urlFundacion});
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al cargar datos de las APIs.");
    }
}




// Método para obtener datos de la API
private JSONArray obtenerDatosDeApi(String urlString) throws IOException, JSONException {
    URL url = new URL(urlString);
    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    connection.setRequestMethod("GET");
    //connection.setRequestProperty("Authorization", "Token " + token); // Asumiendo que se usa un token de autenticación
    connection.setRequestProperty("Authorization", "Token " + token2);
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
        return new JSONArray(response.toString());
    } else {
        throw new IOException("Error en la conexión. Código de respuesta: " + responseCode);
    }
}
//------------------------------------------FIN LISTAR FUNDACIONES-------------------------------------------------------------------------

//------------------------------------------INICIO AGREGAR FUNDACIONES----------------------------------------------------------------------------
private void agregarFundacion() {
    String urlAPI = "http://127.0.0.1:8000/api/fundacion/"; // URL de la API para agregar fundación

    // Obtener datos de los campos de texto
    String nombre = txtNombre.getText().trim();
    String descripcion = txtDescrip.getText().trim();
    String urlFundacion = txtURLFunda.getText().trim();

    if (nombre.isEmpty() || descripcion.isEmpty() || urlFundacion.isEmpty() || selectedImageFile == null) {
        JOptionPane.showMessageDialog(null, "Todos los campos son obligatorios, incluyendo la imagen.");
        return;
    }

    try {
        // Preparar cliente HTTP
        OkHttpClient client = new OkHttpClient();

        // Crear el cuerpo de la imagen
        RequestBody imageBody = RequestBody.create(selectedImageFile, MediaType.parse("image/*"));

        // Crear el cuerpo de la solicitud multipart
        MultipartBody requestBody = new MultipartBody.Builder()
            .setType(MultipartBody.FORM)
            .addFormDataPart("nombre", nombre)
            .addFormDataPart("desc_fundacion", descripcion)
            .addFormDataPart("url_fundacion", urlFundacion)
            .addFormDataPart("imagen", selectedImageFile.getName(), imageBody)
            .build();

        // Construir la solicitud HTTP
        Request request = new Request.Builder()
            .url(urlAPI)
            .post(requestBody) // Método POST
            //.addHeader("Authorization", "Token " + token) // Si se requiere autenticación
            .addHeader("Authorization", "Token " + token2)
            .build();

        // Ejecutar la solicitud
        okhttp3.Response response = client.newCall(request).execute();

        // Manejar la respuesta
        if (response.isSuccessful()) {
            JOptionPane.showMessageDialog(null, "Fundación agregada exitosamente.");
            cargarDatosTabla();
        } else {
            JOptionPane.showMessageDialog(null, "Error al agregar la fundación. Código de respuesta: " + response.code());
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al realizar la solicitud.");
    }
}



private File selectedImageFile; // Variable global para almacenar la imagen seleccionada

private void seleccionarImagen() {
    // Crear un selector de archivos
    JFileChooser fileChooser = new JFileChooser();
    fileChooser.setDialogTitle("Seleccionar Imagen");
    fileChooser.setFileFilter(new FileNameExtensionFilter("Imágenes", "jpg", "png", "jpeg", "gif"));

    // Abrir el diálogo y obtener la respuesta del usuario
    int result = fileChooser.showOpenDialog(this);
    if (result == JFileChooser.APPROVE_OPTION) {
        selectedImageFile = fileChooser.getSelectedFile(); // Guardar el archivo seleccionado
        String filePath = selectedImageFile.getAbsolutePath();

        // Mostrar la ruta seleccionada en el campo de texto (opcional)
        txtImagenUrl.setText(filePath);

        // Mostrar una vista previa de la imagen (opcional)
        ImageIcon icon = new ImageIcon(new ImageIcon(filePath).getImage()
                           .getScaledInstance(150, 150, Image.SCALE_DEFAULT));
        JOptionPane.showMessageDialog(this, "", "Vista Previa", JOptionPane.INFORMATION_MESSAGE, icon);
    }
}



//------------------------------------------FIN AGREGAR FUNDACIONES------------------------------------------------------------------------

//-------------------------------------------------------------------INICIO ELIMINAR FUNDACIONES------------------------------------------------------------------    

// Método para eliminar una fundación a través de la API
private void eliminarFundacion(int fundacionId) {
    String urlString = "http://127.0.0.1:8000/api/fundacion/" + fundacionId + "/"; // URL de la API para eliminar la fundación

    try {
        // Crear la URL y la conexión
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Configurar el método DELETE y los encabezados
        connection.setRequestMethod("DELETE");  // Cambiar a DELETE para eliminar
        //connection.setRequestProperty("Authorization", "Token " + token);  // Token de autenticación
        connection.setRequestProperty("Authorization", "Token " + token2);
        connection.setRequestProperty("Accept", "application/json");

        // Conectar y obtener la respuesta
        connection.connect();
        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_NO_CONTENT) {
            JOptionPane.showMessageDialog(null, "Fundación eliminada correctamente.");
            // Aquí puedes actualizar la tabla o hacer otras acciones
        } else {
            JOptionPane.showMessageDialog(null, "Error al eliminar fundación. Código de respuesta: " + responseCode);
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al eliminar fundación.");
    }
}

// Método común para manejar la eliminación de una fundación
private void manejarEliminacionFundacion() {
    // Obtener la fila seleccionada
    int filaSeleccionada = TablaFundaciones.getSelectedRow();

    if (filaSeleccionada != -1) {
        // Obtener el ID de la fundación en la primera columna (suponiendo que el ID está en la columna 0)
        int fundacionId = (int) TablaFundaciones.getValueAt(filaSeleccionada, 0);

        // Mostrar un cuadro de confirmación para eliminar la fundación
        int confirmacion = JOptionPane.showConfirmDialog(null, 
            "¿Está seguro de que desea eliminar esta fundación?", 
            "Confirmar eliminación", 
            JOptionPane.YES_NO_OPTION);

        if (confirmacion == JOptionPane.YES_OPTION) {
            eliminarFundacion(fundacionId); // Llamar al método de eliminación
            cargarDatosTabla();  // Recargar la tabla para reflejar la eliminación
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione una fundación de la tabla.");
    }
}


//-------------------------------------------------------------------FIN ELIMINAR FUNDACIONES------------------------------------------------------------------    
   

//-------------------------------------------------------------------INICIO MODIFICAR FUNDACIONES-------------------------------------------------------

// Método para modificar la fundación, que ahora incluye la opción de cambiar la imagen
private void modificarFundacion(int fundacionId) {
    String urlString = "http://127.0.0.1:8000/api/fundacion/" + fundacionId + "/"; // URL de la API para modificar la fundación

    // Obtener los datos de los campos
    String nombre = txtNombre.getText().trim();
    String descripcion = txtDescrip.getText().trim();
    String urlFundacion = txtURLFunda.getText().trim();

    // Verificar que los campos obligatorios no estén vacíos
    if (nombre.isEmpty() || descripcion.isEmpty() || urlFundacion.isEmpty()) {
        JOptionPane.showMessageDialog(null, "Todos los campos son obligatorios.");
        return;
    }

    try {
        // Preparar cliente HTTP
        OkHttpClient client = new OkHttpClient();

        // Crear la solicitud de cuerpo multipart (para enviar tanto texto como archivos)
        MultipartBody.Builder requestBodyBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM)
            .addFormDataPart("nombre", nombre)
            .addFormDataPart("desc_fundacion", descripcion)
            .addFormDataPart("url_fundacion", urlFundacion);

        // Si se ha seleccionado una nueva imagen, agregarla al cuerpo de la solicitud
        if (selectedImageFile != null) {
            RequestBody imageBody = RequestBody.create(selectedImageFile, MediaType.parse("image/*"));
            requestBodyBuilder.addFormDataPart("imagen", selectedImageFile.getName(), imageBody);
        }

        // Construir la solicitud HTTP
        Request request = new Request.Builder()
            .url(urlString)
            .put(requestBodyBuilder.build()) // Método PUT
            //.addHeader("Authorization", "Token " + token) // Si se requiere autenticación
            .addHeader("Authorization", "Token " + token2)
            .build();

        // Ejecutar la solicitud
        okhttp3.Response response = client.newCall(request).execute();

        // Manejar la respuesta
        if (response.isSuccessful()) {
            JOptionPane.showMessageDialog(null, "Fundación modificada exitosamente.");
            cargarDatosTabla(); // Recargar la tabla con los datos actualizados
        } else {
            JOptionPane.showMessageDialog(null, "Error al modificar la fundación. Código de respuesta: " + response.code());
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al realizar la solicitud.");
    }
}

// Método para manejar la modificación de una fundación (confirmar la selección y ejecución)
private void manejarModificacionFundacion() {
    int filaSeleccionada = TablaFundaciones.getSelectedRow(); // Obtener la fila seleccionada en la tabla

    if (filaSeleccionada != -1) {
        int fundacionId = (int) TablaFundaciones.getValueAt(filaSeleccionada, 0); // Obtener el ID del formulario

        // Confirmar la modificación
        int confirmacion = JOptionPane.showConfirmDialog(
            null,
            "¿Está seguro de que desea modificar los datos de esta fundación?",
            "Confirmar modificación",
            JOptionPane.YES_NO_OPTION
        );

        if (confirmacion == JOptionPane.YES_OPTION) {
            // Llamar al método para seleccionar la imagen
            seleccionarImagen();

            // Llamar al método modificarFundacion pasando el ID de la fundación seleccionada
            modificarFundacion(fundacionId);
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione una fundación de la tabla.");
    }
}






//-------------------------------------------------------------------FIN MODIFICAR FUNDACIONES----------------------------------------------------------





//-------------------------------------------------------------------INICIO SELECCIONAR FUNDACIONES-------------------------------------------------------

// Método para seleccionar una fundación y cargar sus datos
private void seleccionarFundacion(int fundacionId) {
    String urlString = "http://127.0.0.1:8000/api/fundacion/" + fundacionId + "/"; // URL de la API para obtener datos de una fundación

    try {
        // Obtener los datos de la fundación desde la API
        JSONObject fundacionObj = obtenerObjetoDeApi(urlString);

        // Procesar y obtener los datos necesarios
        String nombre = fundacionObj.optString("nombre", "N/A");
        String descFundacion = fundacionObj.optString("desc_fundacion", "N/A");
        String imagen = fundacionObj.optString("imagen", "N/A");
        String urlFundacion = fundacionObj.optString("url_fundacion", "N/A");

        // Mostrar los datos en los campos correspondientes
        txtNombre.setText(nombre);
        txtDescrip.setText(descFundacion);
        txtImagenUrl.setText(imagen); // Puedes usar un JLabel con un icono si lo deseas
        txtURLFunda.setText(urlFundacion);

    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al seleccionar la fundación.");
    }
}

// Método para manejar la selección de la fundación en la tabla y cargar los datos
private void manejarSeleccionFundacion() {
    // Obtener la fila seleccionada
    int filaSeleccionada = TablaFundaciones.getSelectedRow();

    if (filaSeleccionada != -1) {
        // Obtener el ID de la fundación en la primera columna (asumiendo que el ID está en la columna 0)
        int fundacionId = (int) TablaFundaciones.getValueAt(filaSeleccionada, 0);

        // Confirmación de selección
        int confirmacion = JOptionPane.showConfirmDialog(
            null,
            "¿Está seguro de que desea cargar los datos de esta fundación?",
            "Confirmar selección",
            JOptionPane.YES_NO_OPTION
        );

        if (confirmacion == JOptionPane.YES_OPTION) {
            try {
                // Llamar al método para cargar los datos de la fundación
                seleccionarFundacion(fundacionId);
            } catch (Exception e) {
                e.printStackTrace();
                JOptionPane.showMessageDialog(null, "Error al manejar la selección de la fundación.");
            }
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione una fundación de la tabla.");
    }
}

// Método para obtener un objeto JSON desde una API (reutilizable)
private JSONObject obtenerObjetoDeApi(String urlString) throws IOException, JSONException {
    URL url = new URL(urlString);
    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    connection.setRequestMethod("GET");
    connection.setRequestProperty("Authorization", "Token " + token); // Autenticación con token
    //connection.setRequestProperty("Authorization", "Token " + token2);
    connection.setRequestProperty("Accept", "application/json");
    connection.connect();

    int responseCode = connection.getResponseCode();
    if (responseCode == HttpURLConnection.HTTP_OK) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }
        reader.close();
        return new JSONObject(response.toString());
    } else {
        throw new IOException("Error en la conexión. Código de respuesta: " + responseCode);
    }
}


//-------------------------------------------------------------------FIN SELECCIONAR FUNDACIONES-----------------------------------------------------------












/**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Fundaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Fundaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Fundaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Fundaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>


        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Fundaciones().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BTAgregarF;
    private javax.swing.JButton BTEliminarP;
    private javax.swing.JButton BTModificarP;
    private javax.swing.JButton BTSeleccionarFund;
    private javax.swing.JButton BTSeleccionarI;
    private javax.swing.JButton BTVolver;
    private javax.swing.JTable TablaFundaciones;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTextField txtDescrip;
    private javax.swing.JTextField txtImagenUrl;
    private javax.swing.JTextField txtNombre;
    private javax.swing.JTextField txtURLFunda;
    private javax.swing.JLabel txtUsuario;
    // End of variables declaration//GEN-END:variables
}
