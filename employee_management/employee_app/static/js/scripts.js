        document.getElementById('employeeForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Obtener los valores del formulario
            const nombre = document.getElementById('nombre').value;
            const cargo = document.getElementById('cargo').value;
            const proyecto = document.getElementById('proyecto').value;
            
            // Validar que todos los campos estén llenos
            if (!nombre || !cargo || !proyecto) {
                alert('Por favor, complete todos los campos.');
                return;
            }
            
            // Mostrar mensaje de éxito
            const successMessage = document.getElementById('successMessage');
            successMessage.style.display = 'block';
            
            // Aquí puedes agregar la lógica para enviar los datos al servidor
            console.log('Datos del empleado:', {
                nombre: nombre,
                cargo: cargo,
                proyecto: proyecto,
                fecha: new Date().toISOString()
            });
            
            // Limpiar el formulario después de 2 segundos
            setTimeout(() => {
                document.getElementById('employeeForm').reset();
                successMessage.style.display = 'none';
            }, 2000);
        });

        // Animación suave para los campos cuando se enfocan
        const inputs = document.querySelectorAll('.form-input, .form-select');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentNode.style.transform = 'scale(1.02)';
            });
            
            input.addEventListener('blur', function() {
                this.parentNode.style.transform = 'scale(1)';
            });
        });
