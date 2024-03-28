function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
       let restaurants = Array.from(document.querySelectorAll('#inputs textarea'));
       let restaurantArray = JSON.parse(restaurants[0].value);

       let restaurantObj = {};

       for (const restaurant of restaurantArray) {
           let [restaurantName, workers] = restaurant.split(' - ');

           if (!Object.keys(restaurantObj).includes(restaurantName)) {
               restaurantObj[restaurantName] = {
                   totalSalary: 0,
                   bestSalary: 0,
                   workers: {}
               }

           }

           workers = workers.split(', ');

           for (const worker of workers) {
               let [workerName, salary] = worker.split(' ');
               restaurantObj[restaurantName]['totalSalary'] += Number(salary);
               restaurantObj[restaurantName]['workers'][workerName] = Number(salary);

               if (Number(salary) > restaurantObj[restaurantName]['bestSalary']) {
                   restaurantObj[restaurantName]['bestSalary'] = Number(salary);
               }
           }

           let bestRestaurant = {
               'name': '',
               'averageSalary': 0,
               'bestSalary': 0,
               'workers': {}
           }

           for (const restaurantName of Object.keys(restaurantObj)) {
               let workersCount = Object.keys(restaurantObj[restaurantName]['workers']).length;
               let avarageSalary = restaurantObj[restaurantName]['totalSalary'] / workersCount;

               if (avarageSalary > bestRestaurant['averageSalary']) {
                   bestRestaurant['name'] = restaurantName;
                   bestRestaurant['averageSalary'] = avarageSalary;
                   bestRestaurant['bestSalary'] = restaurantObj[restaurantName]['bestSalary'];
                   bestRestaurant['workers'] = restaurantObj[restaurantName]['workers'];
               }

           }

           let sortedWorkers = Object.entries(bestRestaurant['workers']);
           sortedWorkers.sort((a,b) => b[1] - a[1]);
           sortedWorkers = Object.fromEntries(sortedWorkers);

           bestRestaurant['workers'] = sortedWorkers;
           
           let bestRestaurantInfo = `Name: ${bestRestaurant['name']} Average Salary: ${ bestRestaurant['averageSalary'].toFixed(2)} Best Salary: ${bestRestaurant['bestSalary'].toFixed(2)}`
           let bestWorkersInfo = [];

           for (const [workerName, salary] of Object.entries(bestRestaurant['workers'])) {
               bestWorkersInfo.push(`Name: ${workerName} With Salary: ${salary}`);
           }

           bestWorkersInfo = bestWorkersInfo.join(' ');

           let paragraph1 = document.querySelector('#bestRestaurant p');
           paragraph1.textContent = bestRestaurantInfo;

           let paragraph2 = document.querySelector('#workers p');
           paragraph2.textContent = bestWorkersInfo;
       }


   }
}