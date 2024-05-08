<?php
/*
Plugin Name: Gradio
Description: Embeds a locally running Gradio app in an iframe within WordPress.
Version: 1.0
Author: Parsa
*/

// Hook for adding admin menus
add_action('admin_menu', 'gradio_iframe_menu');

// Action function for above hook
function gradio_iframe_menu() {
    add_menu_page('Gradio App', 'Gradio App', 'manage_options', 'gradio-iframe-plugin', 'gradio_iframe_page');
}

// Function to display the iframe
function gradio_iframe_page() {
    ?>
    <div style="height: 800px;">
        <iframe src="http://localhost:7860" style="width: 100%; height: 100%; border: none;"></iframe>
    </div>
    <?php
}
?>
