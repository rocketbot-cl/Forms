# Forms
Module to read queues and form data from R.O.C

![alt text](https://raw.githubusercontent.com/rocketbot-cl/Forms/master/example/forms.png)

![alt text](https://raw.githubusercontent.com/rocketbot-cl/Forms/master/example/queues.png)

Como obtener información enviada desde el robot hacia el formulario, agregar este código en la pestaña JS del editor de formulario, tambien agregar la siguiente librería en el campo CDN  ```//cdn.jsdelivr.net/npm/sweetalert2@11```.

Por último activar la opción _Send API_ y agregar en el robot la variable __xperience__ para obtener el token de respuesta 

```js
$(document).ready(function() {
    var params = new URLSearchParams(location.search);
    if (params.has('xperience')) {
        var interval = null;
        swal.fire({
            text: 'Esperando respuesta del Robot...',
            title: 'Por favor espere',
            icon: 'info',
            timer: 15000
        })
        interval = setInterval(function() {
            $.post(
                '../api/form/getExtra',
                $.param({
                    xperience: params.get('xperience')
                }), {
                    headers: {
                        'content-type': 'application/x-www-form-urlencoded'
                    }
                }).done(function(data) {
                if (data.success && data.data) {
                    swal.fire({
                        title: 'Respuesta Recibida',
                        text: data.data
                    })
                    clearInterval(interval)
                }
            })
        }, 10000)
    }
})
```


## Updates
### 03-Aug-2021
- Fixed ApiKey Problems

<h2>License</h2>

<p><a href="http://badges.mit-license.org" rel="nofollow"><img src="https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265" alt="License" data-canonical-src="http://img.shields.io/:license-mit-blue.svg?style=flat-square" style="max-width:100%;"></a></p>

<ul>
  <li><strong><a href="http://opensource.org/licenses/mit-license.php" rel="nofollow">MIT license</a></strong></li>
</ul>
