# MSDS460 - Assignment-2

After many years of working for others, you have decided to start your own data science and software engineering firm. You will offer your services to other organizations as a sole proprietor and independent contractor. A first step in obtaining clients is often to respond to requests for proposal. 

This assignment concerns a development project. Suppose a group of restaurant owners in Marlborough, Massachusetts is requesting a project proposal. They want to know how fast you can develop a new software product and how much it will cost.

You need to propose a consumer-focused recommendation system for more than one hundred restaurants in Marlborough, Massachusetts, as shown in the enclosed file: restaurants-v001.json Download restaurants-v001.json. Data for the project will consist of Yelp reviews of these restaurants. This list of restaurants should be updated monthly, with Yelp reviews updated daily. Given the limitations of open-source Yelp reviews, it is likely that a contract will be obtained to access large quantities of Yelp data through its GraphQL API.

The client requires selected software components for the project. In particular, the client asks that the product recommendation system be implemented using Alpine.js and Tailwind on the frontend, a GraphQL API, and a Go web and database server on the backend. Go, Python, or R may be employed for recommender system analytics on the backend, with persistent storage provided by PostgreSQL, EdgeDB, or PocketBase. The system should be accessible from any modern web browser and may be hosted on a major cloud platform such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP). 

While you expect to be involved in all aspects of the recommender system, you realize that the nature of the project calls for a software development team. You will need to hire people to fill various roles, including frontend developer, backend developer, data engineer, and database administrator, while you fill data science and project management roles.  

The project consists of the eight general tasks, and one of these general tasks, develop product prototype, comprises eight software development subtasks. An Excel spreadsheet shows fifteen tasks with their immediate predecessors: project-plan-v003.xlsx Download project-plan-v003.xlsx  Numerous columns are defined for workers assigned to the project. These columns may prove useful in activity/task scheduling in the future, but they are not used in the critical path analysis itself. Entries in these columns can be integers indicating the numbers of workers of each type assigned to the activity.

Determine best-case, expected, and worst-case estimates for the number of hours needed for each of the sixteen tasks. Also, determine an hourly rate associated with each worker role. These rates can be hourly rates (excluding benefits) that you would expect people in the roles to earn. Assume that all members of the team, like yourself, are working as independent contractors.

**Project Plan**

taskID	task	predecessorTaskIDs	bestCaseHours	expectedHours	worstCaseHours	projectManager	frontendDeveloper	backendDeveloper	dataScientist	dataEngineer
A	Describe product		1	2	3	$62 	$62 	$62 	$62 	$62 
B	Develop marketing strategy		2	4	6	$62 	$62 	$62 	$62 	$62 
C	Design brochure	A	3	6	9	$62 	$62 	$62 	$62 	$62 
D	Develop product  prototype									
D1	    Requirements analysis	A	40	80	120	$62 	$62 	$62 	$62 	$62 
D2	    Software design	D1	80	120	160	$62 	$62 	$62 	$62 	$62 
D3	    System design	D1	80	120	160	$62 	$62 	$62 	$62 	$62 
D4	    Coding	D2, D3	480	720	960	$62 	$62 	$62 	$62 	$62 
D5	    Write documentation	D4	40	80	120	$62 	$62 	$62 	$62 	$62 
D6	    Unit testing	D4	120	160	240	$62 	$62 	$62 	$62 	$62 
D7	    System testing	D6	120	160	240	$62 	$62 	$62 	$62 	$62 
D8	    Package deliverables	D5, D7	40	80	120	$62 	$62 	$62 	$62 	$62 
E	Survey potential market	B, C	20	40	60	$62 	$62 	$62 	$62 	$62 
F	Develop pricing plan	D8, E	16	32	48	$62 	$62 	$62 	$62 	$62 
G	Develop implementation  plan	A, D8	8	16	24	$62 	$62 	$62 	$62 	$62 
H	Write client proposal	F, G	16	24	32	$62 	$62 	$62 	$62 	$62 ![image](https://github.com/user-attachments/assets/e0fb0b2f-55e7-44dc-8d19-7216cd279afd)
