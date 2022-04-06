document.addEventListener('DOMContentLoaded', function() {

    //alert('loaded');

  

    document.querySelectorAll('.edit').forEach(btn => {

        btn.addEventListener('click', function() { 

            //alert(btn.dataset.vehicle);

            const vehicleId = btn.dataset.vehicle;
            const descr = document.querySelector(`.descr[data-vehicle="${vehicleId}"]`);

            // inser value that comes back from server
            descr.innerHTML = "flushed description :)"
        })
        
        


    })

})