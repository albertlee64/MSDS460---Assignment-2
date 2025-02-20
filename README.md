# MSDS460 - Assignment-2

The Project Plan (version 8)

Developed by Thomas W. Miller. Revised January 30, 2025.

After many years of working for others, you have decided to start your own data science and software engineering firm. You will offer your services to other organizations as a sole proprietor and independent contractor. A first step in obtaining clients is often to respond to requests for proposal. 

This assignment concerns a development project. Suppose a group of restaurant owners in Marlborough, Massachusetts is requesting a project proposal. They want to know how fast you can develop a new software product and how much it will cost.

You need to propose a consumer-focused recommendation system for more than one hundred restaurants in Marlborough, Massachusetts, as shown in the enclosed file: restaurants-v001.json Download restaurants-v001.json. Data for the project will consist of Yelp reviews of these restaurants. This list of restaurants should be updated monthly, with Yelp reviews updated daily. Given the limitations of open-source Yelp reviews, it is likely that a contract will be obtained to access large quantities of Yelp data through its GraphQL API.

The client requires selected software components for the project. In particular, the client asks that the product recommendation system be implemented using Alpine.js and Tailwind on the frontend, a GraphQL API, and a Go web and database server on the backend. Go, Python, or R may be employed for recommender system analytics on the backend, with persistent storage provided by PostgreSQL, EdgeDB, or PocketBase. The system should be accessible from any modern web browser and may be hosted on a major cloud platform such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). 

While you expect to be involved in all aspects of the recommender system, you realize that the nature of the project calls for a software development team. You will need to hire people to fill various roles, including frontend developer, backend developer, data engineer, and database administrator, while you fill data science and project management roles.  

The project consists of the eight general tasks, and one of these general tasks, develop product prototype, comprises eight software development subtasks. An Excel spreadsheet shows fifteen tasks with their immediate predecessors: project-plan-v003.xlsx Download project-plan-v003.xlsx  Numerous columns are defined for workers assigned to the project. These columns may prove useful in activity/task scheduling in the future, but they are not used in the critical path analysis itself. Entries in these columns can be integers indicating the numbers of workers of each type assigned to the activity.

Determine best-case, expected, and worst-case estimates for the number of hours needed for each of the sixteen tasks. Also, determine an hourly rate associated with each worker role. These rates can be hourly rates (excluding benefits) that you would expect people in the roles to earn. Assume that all members of the team, like yourself, are working as independent contractors.

**Project Plan**

![image](https://github.com/user-attachments/assets/e0fb0b2f-55e7-44dc-8d19-7216cd279afd)

**Network Diagram**

p.plot_network_diagram(plot_type = 'nx')

![image](https://github.com/user-attachments/assets/6ef2403b-6a92-4a77-8853-871e9225345e)

**Linear Programming**

Using LP PuLP Python Library to determine the total minimum project duration.

Decision Variables: Start times for each task and completion times

Objective Function: Minimize the Total Project Duration

Constraints: Predecessor Tasks and non-negative start times

 model = LpProblem('Project_Scheduling', LpMinimize)

![image](https://github.com/user-attachments/assets/65c1f172-75a9-4c36-8b02-1dff09aa526b)

**Gantt Chart for Expected Hours**

![image](https://github.com/user-attachments/assets/1f80eddd-70c8-4f03-b427-e112bb67a348)

**Solution & Proposal**

For the delivery of a custom software/application that creates a consumer-focused recommendation system for more than 100 hundred restaurants in the Marlborough, MA area, I would charge a Fixed Price contract of $860,000 with a delivered prototype in 42 weeks completion (or 1,680 hours). Realistically, a prototype could be done in short as 35 weeks BUT the 7 extra weeks allows provides slack within the project timeline. If additional subcontractors were considered, then the project could be done sooner but at a higher cost. Because it’s a Fixed Price contract, any delays to the project beyond the 42 weeks, the company will absorb the additional costs. Typical projects like this can last between ~5 to ~11 months. I am confident that the team can complete this within 42 weeks. If the client requires a Hypercare support period seen in many product releases like this, that would come at additional costs and a new SoW (Statement of Work) would need to be developed.


**ChatGPT Usage**

Leveraged ChatGPT to help develop the linear programmming model using Python PuLP. ChatGPT also helped with determining the optimal for the worst case and best case along with creating the Gantt Chart. ChatGPT conversation attached.
