# BudgetTech
<p align="center">
    <img src="https://i.imgur.com/c1BF8T7.png" alt="Logo" width="200">
    <br>
    The First Arabic FinTech ChatBot, build Using AI to Help You Saving Your Money.
    <br />
    <a href="http://8.213.17.11/">View Demo</a>
  </p>
</p>

# Tools and Technology's Used
## 1- Application Tools 🎯
- In the <b>backend</b> we used is [Flask](https://palletsprojects.com/p/flask/) Python web framework which help us to use the AI model.
- In the <b>frontend</b> for now we used pure HTML,CSS and JavaScript.
- The <b>database</b> we used is [Postgres](https://www.postgresql.org/) database, is open source database and best option for microservices.
## 2- AI Tools 👾
- On AI side we used [Tensorflow](https://www.tensorflow.org/) tool on Python for training and testing the model.
## 3- Containerization & Microservices 🐬
- We are running the application as container using [Docker](https://www.docker.com/), which help us fast building and running on any environment.
- We manage the containers by using [Kubernetes](https://kubernetes.io/), which help us to create cluster for the application and implement the CICD and high availability by scaling the nodes.
## 4- CI/CD ♾️
- We implemented the continuous integration and continuous deployment (<b>CI/CD</b>) methodology, which help us to automate the testing & deployment the new changes.
- We used [GitHub Action](https://github.com/features/actions) for integration and to running the automation pipelines
- For delivering the new build to production, we used [ArgoCD](https://argo-cd.readthedocs.io/en/stable), which help us syncing the [GitOps](https://www.gitops.tech/) and deploy it into Kubernetes cluster.
## 5- Cloud Deployment ☁️
- We used [Alibaba Cloud](https://www.alibabacloud.com/) to host our application.
- We used [Terraform](https://www.terraform.io/) tool for automate the infrastructure building on cloud. 
<br>
<br>

# Running The Application Using Docker 🐬
To run the application, you should have Postgres running first, below example of running Postgres database with Docker.
``` shell
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=hardpass123 -e POSTGRES_USER=ricko -e POSTGRES_DB=chatbot postgres:14 pg_db
```
After running Postgres db, you ready now to run our project. Clone the repository on your machine.
``` shell
git clone https://github.com/Ahmad-Faqehi/budge-tech.git
cd budge-tech/
```
Start build the docker image by following execute the following command.
``` shell
docker build ./application/ -t budget-tech
```
After finish the building, you can start the container using the following command.
``` shell
docker run -d -p 80:5000 -e DB_HOST=pg_db -e DB_NAME=chatbot -e DB_USER=ricko -e DB_PASSWORD=hardpass123 budget-tech
```
Now, you can access the application by opening the following url:
<br>
http://localhost/
<br>
<br>
# Acknowledgments ✨
Thanks goes to these wonderful people who made the impossible done
- [Samirah Alhusayni](https://www.linkedin.com/in/samirah-alhusayni-/)
- [Abduljawad Kuaitan](https://www.linkedin.com/in/abduljawad-kuaitan-83a7471a8/)
- [Shahad Alameel](https://www.linkedin.com/in/shahadalameel/)
- [Abdullah Alshamrani](https://www.linkedin.com/in//)
<br>
<br>
<!-- CONTACT -->
## Contact

[Ahmad Faqehi](https://www.linkedin.com/in/ahmad-faqehi/) - [@A_F775](https://twitter.com/A_F775) - alfaqehi775@hotmail.com

Project Link: [https://github.com/Ahmad-Faqehi/budge-tech](https://github.com/Ahmad-Faqehi/budge-tech)
