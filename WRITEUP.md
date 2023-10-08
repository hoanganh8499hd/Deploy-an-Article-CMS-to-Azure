# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*

    I tried calculating from URL: https://azure.microsoft.com/en-in/pricing/calculator/ and get result
        1. Virtual Machine: Estimated monthly cost $108.42 with:
            A2: 2 Cores, 3.5 GB RAM, 60 GB Temporary storage, $0.133/hour and used 730 hours (License included)
            Managed Disks : 1 Standard HDD -- S15: 256 GiB, $11.328/month
        2. App Service: Estimated monthly cost $54.75
            Region: West US, Operating system: Windows, Tier: Basic
            INSTANCE: B1: 1 Cores(s), 1.75 GB RAM, 10 GB Storage, $0.075 and used 730 hours
            No SSL Connections

    Scalability:
        App Services can dynamic scaling without config manual, when use VM, you have to config manually and manage scaling .

    Availability:
        App Service and VM can both provide high availability. App Service is build-in feature and dynamic. VM requires properly configured and management.

    Workflow:  
        You have more control and config about the underlying infrastructure with VM. With App Service, you can focus more on the application code and it's simpler.

- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
    I choose App Service for my project CMS app because this is uncomplicated and lightweight cms app. Furthermore, App Service offers a more cost-effective solution in my case and i don't need to control and config about the underlying infrastructure.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

In the future, if the application has a lot of user and high traffic or the customer require more control over the operating system, specialized configurations, we will change my decision and choose Virtual Machine instead.