pipeline{
    agent any
    
    options{
        buildDiscarder(logoRotator(numTokeepStr:'3'))
        timestamps()
        timeout(time:30,unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('anilgcpcredentials')
    }


    stages{
        stage('Non Prod Infra : Creation'){
            when{
                anyof{
                    branch 'develop';
                    branch 'test';
                }
            }
            steps{
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud config set project excellent-guide-410011'
                    script{
                        sh 'echo running non prod terraform scripts'
                        if(env.BRANCH_NAME == 'develop'){
                            dir("ops/ArtifactRegistry/dev"){
                                sh 'terraform --version'
                                //sh 'terraform init -backend-config=./environment/sit/backend_config.tfvars'
                                //sh 'terraform refresh -var-file=./environment/sit/variables.tfvars -no-color'
                                //env.TERRAFORM_PLAN_EXIT_CODE = sh(returnStatus: true, script:"terraform plan -var-file=./sit/variables.tfvars -no-color -detailed-exitcode -out=output.tfplan")
                                //sh 'terraform apply -var-file=./environment/sit/variables.tfvars -no-color -auto-approve'
                            }
                        } else if(env.BRANCH_NAME == 'test'){
                            dir("ops/ArtifactRegistry/uat"){
                                sh 'terraform --version'
                                sh 'terraform init -backend-config=./environment/uat/backend_config.tfvars'
                                sh 'terraform refresh -var-file=./environment/uat/variables.tfvars -no-color'
                                env.TERRAFORM_PLAN_EXIT_CODE = sh(returnStatus: true, script:"terraform plan -var-file=./uat/variables.tfvars -no-color -detailed-exitcode -out=output.tfplan")
                                sh 'terraform apply -var-file=./environment/uat/variables.tfvars -no-color -auto-approve'
                            }
                        }
                    }
                
            }
        }
        stage('Production Infra : Creation'){
            when{
                branch 'main';
            }
            steps{
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud config set project excellent-guide-410011'
                {
                    script{
                        sh 'echo running prod terraform scripts'
                        if(env.BRANCH_NAME == 'main'){
                            dir("ops/ArtifactRegistry/prod"){
                                sh 'terraform --version'
                                sh 'terraform init -backend-config=./environment/prd/backend_config.tfvars'
                                sh 'terraform refresh -var-file=./environment/prd/variables.tfvars -no-color'
                                env.TERRAFORM_PLAN_EXIT_CODE = sh(returnStatus: true, script:"terraform plan -var-file=./prd/variables.tfvars -no-color -detailed-exitcode -out=output.tfplan")
                                sh 'terraform apply -var-file=./environment/prd/variables.tfvars -no-color -auto-approve'
                            }
                        }
                        
                    }
                }
            }
        }
    }
    post{
        always{
            cleanWs()
        }
    }
}