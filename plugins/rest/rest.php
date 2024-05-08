<?php
/*
Plugin Name: Rest
Description: Sends text to a REST API and displays the response.
Version: 1.0
Author: Parsa
*/

add_action('admin_menu', 'my_plugin_menu');

function my_plugin_menu() {
    add_menu_page('My Plugin Settings', 'API Plugin', 'manage_options', 'my-plugin', 'my_plugin_page');
}


function my_plugin_page() {
    ?>
    <div class="wrap">
        <h2>My API Plugin</h2>
        <form method="post">
            <input type="text" name="input_text" placeholder="Enter text">
            <input type="submit" name="submit" value="Send">
        </form>
    <?php
    if (isset($_POST['submit'])) {
        $response = my_send_api_request($_POST['input_text']);
        echo '<p>Response: ' . esc_html($response) . '</p>';
    }
    echo '</div>';
}


function my_send_api_request($input_text) {
    $api_url = 'http://127.0.0.1:5000/process';

    // Append the text as a query parameter in URL
    $response = wp_remote_post($api_url, array(
        'body'    => json_encode(array('text' => $input_text)),
        'headers' => array('Content-Type' => 'application/json'),
    ));

    if (is_wp_error($response)) {
        return 'API request failed: ' . $response->get_error_message();
    }

    $body = wp_remote_retrieve_body($response);
    return $body;  // Assuming the API returns a string response
}

register_activation_hook(__FILE__, 'my_plugin_activate');

function my_plugin_activate() {
    // Example of a condition: Check for the existence of required functions or classes
    if (!function_exists('wp_remote_post')) {
        deactivate_plugins(plugin_basename(__FILE__)); // Deactivate our plugin
        wp_die('This plugin requires the HTTP API functions, which are not available on this site.');
    }

    // You could also perform a test API request and check for proper response
    $response = wp_remote_post('http://127.0.0.1:5000/process', array(
        'body'    => json_encode(array('text' => 'test')),
        'headers' => array('Content-Type' => 'application/json'),
    ));

    if (is_wp_error($response)) {
        deactivate_plugins(plugin_basename(__FILE__));
        wp_die('API connection test failed. Plugin cannot be activated.');
    }
}