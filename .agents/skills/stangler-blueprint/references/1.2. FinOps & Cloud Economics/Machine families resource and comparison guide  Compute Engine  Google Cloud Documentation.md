---
name: Machine families resource and comparison guide | Compute Engine | Google Cloud Documentation
keywords: (placeholder)
metadata:
  url: https://docs.cloud.google.com/compute/docs/machine-resource
  source: SOURCE_TYPE_WEB_PAGE
  date: 2026-05-16T14:22:32.566Z
  notebook: 1.2. FinOps & Cloud Economics
---
Machine families resource and comparison guide | Compute Engine | Google Cloud Documentation
Skip to main content
docs.cloud.google.com uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more
OK, got it
Technology areas
close
AI and ML
Application development
Application hosting
Compute
Data analytics and pipelines
Databases
Distributed, hybrid, and multicloud
Industry solutions
Migration
Networking
Observability and monitoring
Security
Storage
Cross-product tools
close
Access and resources management
Costs and usage management
Infrastructure as code
SDK, languages, frameworks, and tools
More /
Console
[x] light Light theme [-] dark Dark theme [-] device Device default
Language
English
Deutsch
Español
Español – América Latina
Français
Indonesia
Italiano
Português
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
Sign in 
Compute Engine
Start free
Overview Guides APIs & Reference Samples Resources More
Technology areas
More
Overview
Guides
APIs & Reference
Samples
Resources
Cross-product tools
More
Console
Discover
Product overview
Compute Engine instances
Instance groups
Compute Engine machine resources
Machine resource guide
Machine type families
General-purpose machines
Storage-optimized machines
Compute-optimized machines
Memory-optimized machines
Accelerator-optimized machines
Benchmark VM scores
CPU platforms
GPUs
About GPUs on Google Cloud
GPU machine types
Arm VMs
Bare metal instances
Regions and zones
About regions and zones
Accelerator locations
GPU locations
TPU locations
About AI zones
Global, regional, and zonal resources
Get started
Plan and prepare
Work with regions and zones
View available regions and zones
Manage access to AI zones
Change the default region or zone
Review VM deployment options
Choose a deployment strategy
About VM provisioning models
About VM tenancy
Design resilient systems
Networking overview for VMs
Images and operating systems
OS images
About OS images
Operating system details
OS image lifecycle
Support policy
Premium operating systems
RHEL FAQ
SLES FAQ
Ubuntu Pro FAQ
Microsoft Licensing on Google Cloud
Microsoft licenses FAQ
License Manager
About License Manager
Use License Manager for Microsoft Office
View audit logs
Access control
Access control overview
Manage access to Compute Engine resources
Organization policies
Overview
Managed constraints
Custom constraints
IAM roles and permissions
Service accounts
Name resources
Quickstarts
Create a Linux VM
Create a Windows Server VM
Create a managed instance group
Create instances
Instance creation overview
Create an instance
Create and start an instance
Create with a customized machine configuration
Create with a custom hostname
Create with a custom machine type
Specify a minimum CPU platform for an instance
Create with attached GPUs
About GPU instances
Create overview
Create an A3 Ultra or A4 instance
Create an A3 instance with GPUDirect enabled
Create an A3 High or A2 instance
Create a G2 or G4 instance
Create an N1 instance that has attached GPUs
Install drivers
Install GPU drivers
Install drivers for NVIDIA RTX Virtual Workstations (vWS)
Drivers for NVIDIA RTX Virtual Workstations (vWS)
Create with a customized OS configuration
Create from a public image
Create from a custom image
Create from a shared image
Create using a RHEL BYOS image
Create with a customized networking configuration
Create in a specific subnet
Create with multiple network interfaces
Create with IPv6 addresses
Create an instance that uses Cloud RDMA
Create with a customized observability configuration
Create an instance for Ops Agent monitoring and logging
Enable virtual displays on an instance
Create with a customized security configuration
Create an instance that uses a user-managed service account
Create using an existing configuration
Create using an instance template
Create an instance similar to an existing instance
Create using alternative provisioning models
Create a Flex-start VM
About Flex-start VMs
Create a Flex-start VM
Create a Spot VM
About Spot VMs
Create and use Spot VMs
Create a reservation-bound VM
About reservation-bound VMs
Create a reservation-bound VM
Create an instance that can be preempted
About preemptible VMs
Create and use preemptible VMs
Create instances for specific workload types
Create a Google-configured, workload-optimized instance
Create an HPC-ready instance
Create and manage a Windows Server instance
Create a SQL Server instance
Create custom images
Requirements to build custom images
Create custom images
Create custom Windows BYOL base images
Create custom Windows Server images
Create and manage instance templates
About instance templates
Create instance templates
Deterministic instance templates
Get, list, and delete instance templates
Create multiple VMs
Create a managed instance group (MIG)
Basic scenarios for creating MIGs
Create a MIG in a single zone
Create a MIG in multiple zones in a region
Create a MIG with multiple machine types
Create a MIG from an existing VM
Create a MIG with autoscaling
Create a MIG with preemptible VMs
Create a MIG with GPU VMs
Create a MIG with stateful configuration
Bulk creation of VMs
About bulk creation of VMs
Create VMs in bulk
Create GPU VMs in bulk
Configure instance flexibility for VMs created in bulk
Instance flexibility for VMs created in bulk
Create VMs in bulk with instance flexibility
Create HPC clusters with enhanced cluster management capabilities
Overview of HPC cluster creation with H4D machine series
Reserve capacity through your account team
View reserved capacity for H4D instances
Create an H4D Slurm cluster with enhanced management capabilities
Bulk create HPC-optimized instances that use RDMA with enhanced management capabilities
Create a HPC MIG with H4D machine series
Examples for creating MIGs with H4D machine series
Create a MIG with H4D machine types and flex-start
Create a MIG for HPC workloads with reservation-bound consumption
Create sole-tenant VMs
Sole-tenancy overview
Create sole-tenant node templates
Create sole-tenant node groups
Provision a sole-tenant VM
Advanced maintenance control for sole-tenant nodes
Sole-tenancy best practices
Sole-tenancy accounting FAQ
Create a virtual workstation
About creating virtual workstations
Create a virtual Linux workstation
Create a virtual Windows workstation
Create a virtual Linux workstation with an attached GPU
Create a virtual Windows workstation with an attached GPU
Use nested virtualization
About nested virtualization
Manage the nested virtualization constraint
Enable nested virtualization
Create nested VMs
Manage VM boot disks
Detach and reattach a boot disk
Create a customized boot disk
Migrate VMs
Choose a migration path
Bring your own licenses
Import disks and images
Prerequisites for importing and exporting VM images
Automatic import
Import virtual disks
Import virtual appliances
Manual import
Manually import boot disks
Manually configure imported disks
Create a persistent disk image from an ISO file
Move a VM within Google Cloud
Move a VM between zones
Migrate a VM between networks
Copy VMs between projects
Move an existing VM to a new VM
Connect to VMs
Connect to a VM
About SSH connections
Linux VMs
Connect to VMs
Connect through internal IP addresses
Connection options for internal-only VMs
Connect using IAP
Connect using a bastion host
Connect using Cloud VPN
Connect as the root user
Connect using service accounts
Configure apps to use SSH
Best practices
Securely connect to VMs
Windows VMs
Connect to Windows VMs using RDP
Connect to a Windows VM's SAC
Connect to Windows VMs using SSH
Connect to Windows VMs using PowerShell
Manage access to VMs
Linux VMs
Choose an access management method
About OS Login
Set up OS Login
Set up OS Login to require SSH certificates
Enable security keys with OS Login
Manage OS Login in an organization
Monitor OS Login audit logs
Windows VMs
Manage accounts and credentials on Windows VMs
Automate Windows password generation
Manually manage SSH keys
Create SSH keys
Add SSH keys to VMs
Restrict SSH keys from VMs
Best practices for securing SSH access
Overview
Control network access
Control SSH login access
Protect SSH credentials
Audit SSH access
Manage tags for resources
Transfer files to or from a VM
Transfer files to Linux VMs
Transfer files to Windows VMs
IP addresses
Internal DNS
Overview of internal DNS
Access VMs using internal DNS names
Use zonal DNS
Overview of zonal DNS
Set zonal DNS as the default
Migrate to zonal DNS
Monitor DNS failure rates
Create a PTR record for a VM
Verify VM identity
Manage storage
Choose a disk type
Disk types
About Hyperdisk
Hyperdisk overview
Choose a Hyperdisk type
Hyperdisk Balanced
Hyperdisk Balanced High Availability
Hyperdisk Extreme
Hyperdisk ML
Hyperdisk Throughput
About Persistent Disk
Extreme Persistent Disk
About Local SSD
Use pools to manage capacity and performance
About Hyperdisk pools
Choose a Hyperdisk pool type
Hyperdisk Storage Pools
Hyperdisk Exapools
Create a Hyperdisk pool
Manage Hyperdisk pools
Add disks to VMs
Create a VM with Local SSD disks
Create a VM with additional non-boot disks
Create a new Hyperdisk
Create a new Persistent Disk
Add disks from a storage pool to VMs
Share a disk between VMs
Attach a disk to a VM
Mount in-memory RAM disks
Configure disks
Format and mount a non-boot disk on Linux
Format and prepare a non-boot disk on Windows
Access disks attached to a VM
Best practice: Use persistent device names
Symbolic links to disks
Transfer data to disks attached to a VM
Transfer files to Linux VMs
Transfer files to Windows VMs
View disk details
Encrypt disks
About disk encryption
Encrypt disks with customer-supplied encryption keys
Help protect resources by using Cloud KMS keys
Modify disks
Modify a Hyperdisk
Change the disk type
Increase the size of a Persistent Disk
Modify a Persistent Disk
Evaluate disk performance
Hyperdisk performance overview
Hyperdisk performance and size limits
Persistent Disk performance overview
Review disk performance
Review disk performance metrics
Analyze provisioned IOPS and throughput
Benchmark disk performance
Benchmark Hyperdisk performance
Benchmark Persistent Disk performance on a Linux VM
Benchmark Persistent Disk performance on a Windows VM
Benchmark Local SSD performance
Make disks highly available
Replicate disks across regions
About Asynchronous Replication
Configure replication
Manage replication
Failover and failback disks
Manage asynchronous disks
Manage consistency groups
Review performance metrics
Cross-zonal synchronous disk replication
About regional disks
Build high availability services using regional disks
Design considerations for resilient workloads with regional disks
Create and manage regional disks
Manage failures for regional disks
Back up and restore
Data protection options
Configure the default backup setting
Back up VMs
Use machine images
About machine images
Create machine images
Import machine images from virtual appliances
Use Backup and DR backup plans
About backup plans
Apply backup plans to new instances
Apply or change backup plans for existing instances
Back up disks
Back up disks in place
About instant snapshots
Create and manage instant snapshots
Copy an instant snapshot to a different location
Back up a disk for disaster recovery
About disk snapshots
Best practices for disk snapshots
Set default storage location for globally scoped snapshots
Set creation and restore locations for regionally scoped snapshots
Create disk snapshots
Manage disk snapshots
Create application consistent snapshots
Create Linux application consistent snapshots
Create a Windows disk snapshot (VSS snapshots)
Schedule disk backups
About snapshot schedules
Create snapshot schedules
Manage snapshot schedules
Configure alerts for snapshot schedules
Duplicate a disk with clones
Restore from a backup
Create VMs from machine images
Restore from a standard snapshot
Restore from instant snapshots
Recover a VM with a corrupted or full disk
Manage VMs
Basic operations and lifecycle
VM instance lifecycle
Schedule VM operations
Schedule a VM to start and stop
Limit the run time of a VM
View VM properties
Check that a VM is running
View a list of VMs
View the details of a VM
View the UUID of a VM
View the topology of a VM
View the source image of a VM
View referrers to VMs
View network configuration of a VM
View the number of visible CPU cores in a VM
Stop or suspend a VM
Stop or suspend VMs overview
Stop or restart a VM
Increase or decrease VM shutdown time
Increase shutdown time
Graceful shutdown overview
Enable graceful shutdown
View graceful shutdown
Disable graceful shutdown
Decrease shutdown time
Suspend or resume a VM
Reset a VM
Update VM details
Rename a VM
Update VM properties
Edit the machine type of a VM
Add or remove GPUs
Change the attached service account
Update the physical location of a VM
About placement policies
Create and apply spread placement policies to VMs
View placement policies
Remove or delete placement policies
Update network configuration for instances
Configure static external IP addresses
Configure static internal IP addresses
Configure IPv6 for instances and instance templates
Update network interfaces
Delete VMs
Delete a VM
Prevent accidental VM deletion
Update VM tenancy
Manage multiple VMs
Manage groups of VMs
Work with managed VMs in a MIG
View info about MIGs and managed instances
Add or remove VMs in a MIG
Limit the run time of VMs in a MIG
Add GPU VMs all at once in a MIG
About resize requests
Create resize requests
View, cancel, or delete resize requests
Define the physical location of VMs
About workload policies
Create workload policies
View workload policies
Remove or delete workload policies
Configure instance flexibility in a MIG
About instance flexibility
Add instance flexibility
View instance flexibility
Change or remove instance flexibility
Distribute VMs across zones in a regional MIG
About regional MIGs
About target distribution shape
Set a target distribution for VMs across zones
Disable and reenable proactive instance redistribution
Manually rebalance a regional MIG
Simulate a zone outage for a regional MIG
Work with suspended and stopped VMs in a MIG
Overview
Manually suspend or stop VMs in a MIG
Accelerate scale out with suspended and stopped VMs
Apply new VM configurations in a MIG
About applying new VM configurations to VMs in a MIG
Automatically apply VM configuration updates
Selectively apply VM configuration updates
Apply configuration updates during repairs
Override instance template properties with an all-instances configuration
Perform one-click OS image upgrades
Maintain high availability during VM failures
About repairing VMs for high availability
Repair a VM when an application fails
Set up an application-based health check and autohealing
Monitor VM health state changes
Disable and enable health state change logs
Repair a VM in an alternate zone
Turn off repairs in a MIG
Support a stateful workload with a MIG
About stateful MIGs
Configure stateful MIGs
Configure a stateful MIG
Configure stateful persistent disks
Configure stateful metadata
Configure stateful IP addresses
Apply, view, and remove stateful configuration
How stateful MIGs work
How operations affect preserved state
Group VMs together
Migrate an existing workload to a stateful managed instance group
Group unmanaged VMs together
Delete a MIG
Manage HPC clusters with enhanced cluster management capabilities
Enhanced HPC cluster management capabilities
View H4D cluster topology
Manage host events across reservations
Manage host events across vms
Report faulty host with H4D machines
Host maintenance events
About host events
Live migration process
Set the host maintenance policy
Query metadata server for notices
Simulate a host maintenance event
Handle GPU host maintenance events
Monitor and plan for a host maintenance event
Manually start host maintenance
Manage metadata
About VM metadata
Predefined metadata keys
Set and remove custom metadata
View and query VM metadata
Set and query guest attributes
Securing VMs
About Shielded VMs
Microsoft Secure Boot certificates expiration guide
About Confidential VMs
Protect resources with VPC Service Controls
Monitor security risks with Security Command Center
Manage operating systems
Guest environment
About the guest environment
Install the guest environment
Guest agent
About the guest agent
Guest agent functionality
Configure the guest agent
Manage operating systems using VM Manager
Manage OS images
Image management best practices
Image families best practices
Access Red Hat Knowledgebase
Manage access to custom images
Set up trusted image policies
Export a custom image to Cloud Storage
Set image versions in an image family
Deprecate a custom image
Delete a custom image
Manage OS packages
Manage licenses
About licenses
Manage licenses
License changes and restrictions
Switch between PAYG and BYOS
Switch Windows Server from BYOL to PAYG
Update licenses after an OS upgrade
Append RHEL ELS licenses
Upgrade from Ubuntu to Ubuntu Pro
Manage VM extensions
About VM Extension Manager
Global VM extension policies
Zonal VM extension policies
Install VM extensions by using extension policies
Manage VM extensions by using extension policies
View VM extension logs
Use startup scripts
Startup scripts overview
Use startup scripts on Linux VMs
Use startup scripts on Windows VMs
Run shutdown scripts
Configure time synchronization
Time synchronization overview
Configure network time protocol (NTP)
Configure accurate time
Enable the virtual random number generator (Virtio RNG)
Deploy workloads
Set up authentication for workloads
Choose a workload authentication method
Authenticate workloads to Google Cloud API using service accounts
Authenticate workloads to other workloads over mTLS
Agent for Compute Workloads overview
Web servers
Deploy an Apache server
Deploy an IIS server
Deploy a Flask server by using Terraform
Applications
Interactive: Build a to-do app with MongoDB
Deploy an ASP.NET application
Set up Joomla
Set up LAMP
Perform blue/green deployments using Cloud Build
Send email from a VM
About sending email
Send email with SendGrid
Send email with Mailgun
Send email with Mailjet
Databases
MySQL
MySQL on Compute Engine
Install MySQL on Compute Engine
Configure MySQL on Compute Engine
Set up client access with a private IP address
Cloning a MySQL database on Compute Engine
Architectures for high availability of MySQL clusters on Compute Engine
Deploying a highly available MySQL 5.6 cluster with DRBD on Compute Engine
PostgreSQL
Set up PostgreSQL on Compute Engine
Set up a PostgreSQL data disk
Set up PostgreSQL with hot standby
SQL Server
Best practices for SQL Server VMs
Create
Create a high-performance SQL Server VM
Add a SQL Server license to an existing Linux server
Add a SQL Server license to an existing Windows server
Configure SQL Server on Google Cloud using Google Cloud NetApp Volumes
Use file storage to configure SQL Server failover cluster instance
Use block storage to configure SQL Server Always On availability groups
Configure
Set up AlwaysOn availability groups using an internal load balancer
Set up AlwaysOn availability groups using a distributed network name
Set up a failover cluster VM that uses S2D
Set up a failover cluster VM with multi-writer disks
Set up a SQL Server cluster on Linux with Always On availability groups and Pacemaker
Migrate
Migrate a SQL Server database from AWS EC2 to Compute Engine
Migrate a SQL Server database from Windows to Linux
Disaster recovery
Disaster recovery for Microsoft SQL Server
Disaster recovery for Microsoft SQL server on Persistent disk
Disaster recovery for Microsoft SQL server on Hyperdisk
Deploying Microsoft SQL Server for multi-regional disaster recovery
Backup SQL Server databases to a Google Cloud Storage bucket
Cloning a Microsoft SQL Server database on Compute Engine
Load test SQL Server using HammerDB
Redis
Deployment Options for Redis on Google Cloud
Containers
Containers on Compute Engine
Deploy containers on VMs and managed instance groups
Configure options to run your container
Transition from the container startup agent
Prepare for the shutdown of the container startup agent
Prevent the creation of VMs that use the container metadata
Migrate containers that were deployed on VMs during VM creation
OpenShift workloads
OpenShift on Google Cloud overview
Plan for OpenShift on Google Cloud
Overview of Cluster Services for OpenShift
Built-in integrations for OpenShift
Best practices for high availability with OpenShift
Disaster recovery for OpenShift on Google Cloud
Disaster recovery strategies for active-passive and active-inactive setups with OpenShift
Microsoft Windows
Windows workloads
Best practices for Windows Server VMs
Setting up Active Directory
Best practices for running Active Directory on Google Cloud
Deploy Microsoft SharePoint Server on Compute Engine
Deploying Microsoft Exchange Server 2016 on Compute Engine
Windows Server
Perform an in-place upgrade of Windows Server
Run Windows Server failover clustering
IBM Spectrum Symphony
Integrate IBM Spectrum Symphony with Google Cloud
Install the Compute Engine Symphony provider
Install the Google Kubernetes Symphony provider
Troubleshoot IBM Spectrum Symphony
Others
Load testing
Distributed load testing using Kubernetes
SSH port forwarding and load testing
Analytics
Monte Carlo methods using Apache Spark
Machine learning
Run TensorFlow inference workloads with TensorRT5 and NVIDIA T4 GPU
Monitor
Monitor logs
View audit logs
View usage reports
View Compute Engine operations
Migrate from activity logs to audit logs
View activity logs
Monitor resources
Monitor VM and sole-tenant node usage
Observe and monitor VMs
Monitor GPU performance
Monitor GPU performance on Linux VMs
Monitor GPU performance on Windows VMs
Monitor disks
Monitor disk health
Monitor the replica states of regional disks
Monitor disks
List of metrics for Pools
Monitor Pools
Monitor reservations
Organize resources using labels
Scale
Autoscale groups of VMs
About autoscaling groups of VMs
Create and manage autoscalers
Scale based on CPU utilization
Scale based on predictions
Scale based on load balancing serving capacity
Scale based on Monitoring metrics
Scale based on schedules
Use an autoscaling policy with multiple signals
Manage autoscalers
Understand autoscaler decisions
View autoscaler logs
Autoscale node groups
Reserve VM capacity
Choose a reservation type
Sharing reservations
Best practices for shared reservations
Allow a project to share reservations
On-demand reservations
About on-demand reservations
Create an on-demand reservation
For a single project
For multiple projects
Combine an on-demand reservation with a CUD
Modify an on-demand reservation
Delete an on-demand reservation
Future reservations
About future reservations
Create a reservation request
For a single project
For multiple projects
Modify a reservation request
Delete a reservation request
Future reservations in calendar mode
About future reservations in calendar mode
Create a reservation request in calendar mode
View reservations or reservation requests
Consume a reservation
Prevent VMs from consuming reservations
Load balancing
About load balancing and scaling
Add an instance group to a load balancer
Request routing to a multi-region external HTTPS load balancer
Cross-region load balancing for Microsoft IIS backends
Set up Internal TCP/UDP Load Balancing
Build reliable and scalable applications
Use autohealing for highly available applications
Use load balancing for highly available applications
Use autoscaling for highly scalable applications
Globally autoscale a web service on Compute Engine
Patterns for scalable and resilient applications
Patterns for using floating IP addresses on Compute Engine
Optimize
Resource utilization
Use recommendations to manage resources
Apply machine type recommendations to VMs
Configure machine type recommendations
Apply machine type recommendations to MIGs
View and apply idle resources recommendations
View and understand VM insights
View and understand MIG insights
Manage idle VM recommendations
Idle VM recommendations overview
View and apply idle VM recommendations
Configure idle VM recommendations
Manage reservation recommendations
Reservation recommendations overview
View and apply idle reservation recommendations
View and apply underutilized reservation recommendations
Configure idle reservation recommendations
Configure underutilized reservation recommendations
Overcommit CPUs on sole-tenant VMs
Manual live migration
About manual live migration
Manually live migrate VMs
Share sole-tenant node groups
Next generation dynamic resource management
Cost savings
Get discounts for committed usage
About commitments and committed use discounts (CUDs)
Resource-based CUDs
Manage resource-based commitments
Renew commitments automatically
Extend commitment terms
Merge and split commitments
Upgrade commitments
Share resource-based CUDs across projects
Get discounts for sustained usage
Disk performance
Optimize Hyperdisk performance
Optimize Persistent Disk performance
Optimize Local SSD performance
Workload performance
Set the number of threads per core
Customize the number of visible CPU cores
Analyze the CPU performance using the PMU
PMU overview
Enable the PMU in VMs
Manage the PMU in VMs
Network performance
Network bandwidth
Use Google Virtual NIC
Use IRDMA network driver
Use IDPF network interface
Configure a VM with higher bandwidth
Reduce latency by using compact placement policies
Optimize TCP network communication
Optimize TCP network performance
Optimize TCP network resiliency
Benchmark higher bandwidth VMs
Optimize app latency with load balancing
Use DPDK to improve network performance
Network performance and GPU VMs
Networking and GPU machines
Use higher network bandwidth
Patterns for using multiple host NICs
Troubleshoot
General tips
Troubleshoot connectivity
Troubleshoot RDP
Troubleshoot SSH
Troubleshoot OS Login
Troubleshoot VMs
Troubleshoot VM operations
Troubleshoot VM creation
Troubleshoot resource availability errors
Troubleshoot bulk API VM creation
Troubleshoot VM reboots and shutdowns
Troubleshoot VM suspension
Troubleshoot VM updates
Troubleshoot unresponsive VMs
Troubleshoot VM startup
Troubleshoot fstab errors
Troubleshoot kernel panic
Collecting core dumps
Rescue an inaccessible VM
Troubleshoot CPU soft lockups
Troubleshoot VM configurations
Troubleshoot Arm VMs
Troubleshoot GPU VMs
Troubleshoot NVIDIA GPU errors
Generate a NVIDIA bug report for Blackwell GPUs
Troubleshoot nested virtualization
Troubleshoot using VM screenshots
Troubleshoot sole-tenant nodes
Troubleshoot VM performance issues
Troubleshoot sudoers files
Troubleshoot Windows VMs
Troubleshoot Windows VMs
Collecting diagnostic information
Troubleshoot using the serial console
Troubleshoot using the serial console
Viewing serial port output
Troubleshoot instance groups
Troubleshoot managed instance groups (MIGs)
Troubleshoot OS management
Troubleshoot licenses
Troubleshoot image import and export
Troubleshooting SLES pay-as-you-go registration
Troubleshooting Ubuntu Pro Registration
Troubleshoot metadata server
Troubleshoot metadata server
Troubleshoot networking issues
Troubleshoot common networking issues
Troubleshoot network drivers
Troubleshoot VM performance issues
Troubleshoot storage
Troubleshoot disk creation
Troubleshoot full disks and disk resizing
Troubleshoot disk encryption
Troubleshoot NVMe disks
Troubleshoot instant snapshots
Troubleshoot standard snapshots
Troubleshoot reservations and commitments
Troubleshoot reservation creation
Troubleshoot reservation consumption
Troubleshooting reservation monitoring
Troubleshoot reservation updates
Troubleshoot future reservation creation and updates
Troubleshoot automatic commitment renewal
Troubleshoot quota errors
Troubleshoot concurrent operation quota errors
Troubleshoot workload authentication
Troubleshoot default service accounts
Troubleshoot workload to workload authentication
AI and ML
Application development
Application hosting
Compute
Data analytics and pipelines
Databases
Distributed, hybrid, and multicloud
Industry solutions
Migration
Networking
Observability and monitoring
Security
Storage
Access and resources management
Costs and usage management
Infrastructure as code
SDK, languages, frameworks, and tools
On this page
Compute Engine terminology
Predefined machine types
Local SSD machine types
Bare metal machine types
Custom machine types
Shared-core machine types
Machine family and series recommendations
General-purpose machine family guide
x86
Arm
Storage-optimized machine family guide
Compute-optimized machine family guide
Memory-optimized machine family guide
Accelerator-optimized machine family guide
Arm
x86
Machine series comparison
GPUs and compute instances
What's next
Home
Documentation
Compute
Compute Engine
Guides
Was this helpful?
Send feedback
Machine families resource and comparison guide Stay organized with collections Save and categorize content based on your preferences. Dismiss Got it
On this page
Compute Engine terminology
Predefined machine types
Local SSD machine types
Bare metal machine types
Custom machine types
Shared-core machine types
Machine family and series recommendations
General-purpose machine family guide
x86
Arm
Storage-optimized machine family guide
Compute-optimized machine family guide
Memory-optimized machine family guide
Accelerator-optimized machine family guide
Arm
x86
Machine series comparison
GPUs and compute instances
What's next
This document describes the machine families, machine series, and machine types that you can choose from to create a virtual machine (VM) instance or bare metal instance with the resources that you need. When you create a compute instance, you select a machine type from a machine family that determines the resources available to that instance.
There are several machine families you can choose from. Each machine family is further organized into machine series and predefined machine types within each series. For example, within the N2 machine series in the general-purpose machine family, you can select the n2-standard-4 machine type.
For information about machine series that support Spot VMs (and preemptible VMs), see Compute Engine instances provisioning models.
Note: This is a list of Compute Engine machine families. For a detailed explanation of each machine family, see the following pages:
General-purpose—best price-performance ratio for a variety of workloads.
Storage-optimized—best for workloads that are low in core usage and high in storage density.
Compute-optimized—designed for high performance computing (HPC) solutions and compute-intensive workloads; offers high performance per core on Compute Engine.
Memory-optimized—ideal for memory-intensive workloads, offering more memory per core than other machine families, with up to 12 TB of memory.
Accelerator-optimized—ideal for massively parallelized Compute Unified Device Architecture (CUDA) compute workloads, such as machine learning (ML) and high performance computing (HPC). This family is the best option for workloads that require GPUs.
Compute Engine terminology
This documentation uses the following terms:
Machine family: A curated set of processor and hardware configurations optimized for specific workloads, for example, General-purpose, Accelerator-optimized, or Memory-optimized.
Machine series: Machine families are further classified by series, generation, and processor type.
Each series focuses on a different aspect of computing power or performance. For example, the E series offers efficient VMs at a low cost, while the C series offer better performance.
The generation is denoted by an ascending number. For example, the N1 series within the general-purpose machine family is the older version of the N2 series. A higher generation or series number usually indicates newer underlying CPU platforms or technologies. For example, the M3 series, which runs on Intel Xeon Scalable Processor 3rd Generation (Ice Lake), is a newer generation than the M2 series, which runs on Intel Xeon Scalable Processor 2nd Generation (Cascade Lake).
Machine type: Every machine series offers at least one machine type. Each machine type provides a set of resources for your compute instance, such as vCPUs, memory, disks, and GPUs. If a predefined machine type does not meet your needs, you can also create a custom machine type for some machine series.
The following sections describe the different machine types.
Predefined machine types
Predefined machine types come with a non-configurable amount of memory and vCPUs. Predefined machine types use a variety of vCPU to memory ratios:
highcpu — from 1 to 3 GB memory per vCPU; typically, 2 GB memory per vCPU.
standard — from 3 to 7 GB memory per vCPU; typically, 4 GB memory per vCPU.
highmem — from 7 to 12 GB memory per vCPU; typically, 8 GB memory per vCPU.
megamem — from 12 to 15 GB memory per vCPU; typically, 14 GB memory per vCPU.
ultramem — from 24 to 31 GB memory per vCPU.
hypermem — from 15 to 24 GB memory per vCPU; typically, 16 GB memory per vCPU.
For example, a c3-standard-22 machine type has 22 vCPUs, and as a standard machine type, it also has 88 GB of memory.
Local SSD machine types
Local SSD machine types are special predefined machine types. The machine type names include lssd . When you create a compute instance using one of the following machine types, Titanium SSD or Local SSD disks are automatically attached to the instance:
-lssd : Available with the C4, C4A, C4D, C3, C3D, and H4D machine series, these machine types attach a predetermined number of 375 GiB Titanium SSD or Local SSD disks to the instance. Examples of this machine type include c4a-standard-4-lssd , c3-standard-88-lssd , and c3d-highmem-360-lssd .
-standardlssd : Available with the storage-optimized Z3 machine series, these machine types provide up to 350 GiB of Titanium SSD disk capacity per vCPU. These machine types are recommended for high performance search and data analysis for medium-sized data sets. An example of this machine type is z3-highmem-22-standardlssd .
-highlssd : Available with the Z3 machine series, these machine types provide between 350 GiB and 600 GiB of Titanium SSD disk capacity per vCPU. These machine types offer high performance and are recommended for storage-intensive streaming and data analysis for large-sized data sets. An example of this machine type is z3-highmem-88-highlssd .
Other machine series also support Local SSD disks but don't use a machine type name that includes lssd . For a list of all the machine types that you can use with Titanium SSD or Local SSD disks, see Choose a valid number of Local SSD disks.
Bare metal machine types
Bare metal machine types are a special predefined machine type. The machine type name includes -metal . When you create a compute instance using one of these machine types, there is no hypervisor installed on the instance. You can attach disks to a bare metal instance, just as you would with a VM instance. Bare metal instances can be used in VPC networks and subnetworks in the same way as VM instances.
Note: Compute Engine bare metal instances aren't related to Bare Metal Solution.
For more information, see Bare metal instances on Compute Engine.
Custom machine types
If none of the predefined machine types match your workload needs, you can create a VM instance with a custom machine type for the N and E machine series in the general-purpose machine family.
Custom machine types cost slightly more to use compared to an equivalent predefined machine type. Also, there are limitations in the amount of memory and vCPUs that you can select for a custom machine type. The on-demand prices for custom machine types include a 5% premium over the on-demand and commitment prices for predefined machine types.
When creating a custom machine type, you can use the extended memory feature. Instead of using the default memory size based on the number of vCPUs you select, you can specify an amount of memory, up to the limit for the machine series.
For more information, see Create a VM with a custom machine type.
Shared-core machine types
The E2 and N1 series contain shared-core machine types. These machine types timeshare a physical core which can be a cost-effective method for running small, non-resource intensive apps.
E2: offers e2-micro , e2-small , and e2-medium shared-core machine types with 2 vCPUs for short periods of bursting.
N1: offers f1-micro and g1-small shared-core machine types which have up to 1 vCPU available for short periods of bursting.
For more information, see CPU bursting.
Machine family and series recommendations
The following tables provide recommendations for different workloads.
Optimized workloads
Storage-optimized
Compute-optimized
Memory-optimized
Accelerator-optimized
Z3
H4D, H3, C2 and C2D
X4, M4, M3, M2, M1
A4X Max, A4X, A4, A3, A2, G4, G2
Highest block storage to compute ratios for storage-intensive workloads
Highest performance and lower cost for high performance computing (HPC), multi-node and compute-bound workloads
Highest memory to compute ratios for memory-intensive workloads
Optimized for accelerated high performance computing workloads
SQL, NoSQL, and vector databases
Data analytics and data warehouses
Search
Media streaming
Large distributed parallel file systems
Manufacturing, weather forecasting, electronic design automation (EDA), High-performance web servers
Healthcare and life sciences, scientific computing
Seismic processing and structural mechanics applications
Modeling and simulation workloads, AI/ML
High-performance web servers, Game Servers
Small to extra-large SAP HANA in-memory databases
In-memory data stores, such as Redis
Simulation
High Performance databases such as Microsoft SQL Server, MySQL
Electronic design automation
Generative AI models such as the following:
Large Language Models (LLM)
Diffusion Models
Generative Adversarial Networks (GAN)
CUDA-enabled ML training and inference
High-performance computing (HPC)
Massively parallelized computation
BERT natural language processing
Deep learning recommendation model (DLRM)
Video transcoding
Remote visualization workstation
After you create a compute instance, you can use rightsizing recommendations to optimize resource utilization based on your workload. For more information, see Applying machine type recommendations for VMs.
General-purpose machine family guide
The general-purpose machine family offers several machine series with the best price-performance ratio for a variety of workloads.
Compute Engine offers general-purpose machine series that run on either x86 or Arm architecture.
x86
The C4 machine series is available on the Intel Granite Rapids and Emerald Rapids CPU platforms and powered by Titanium. C4 machine types are optimized to deliver consistently high performance and scale up to 288 vCPUs, 2.2 TB of DDR5 memory, and 18 TiB of Local SSD. C4 is available in highcpu (2 GB memory per vCPU), standard (3.75 GB memory per vCPU), and highmem (7.75 GB memory per vCPU) configurations. C4 instances are aligned with the underlying non-uniform memory access (NUMA) architecture to offer optimal, reliable, and consistent performance.
The C4D machine series is available on the AMD EPYC Turin CPU platform and powered by Titanium. C4D has a greater max boost frequency as compared with C3D, with improved Instructions Per Clock (IPC) for faster database transactions. By leveraging Hyperdisk storage and Titanium networking, C4D demonstrates up to 55% higher queries per second on Cloud SQL for MySQL and 35% better performance on Memorystore for Redis workloads as compared to C3D. C4D instances are available with up to 384 vCPUs, 3 TB of DDR5 memory, and 12 TiB of Local SSD. C4D is available in highcpu (1.875 GB memory per vCPU), standard (3.875 GB memory per vCPU), and highmem (7.875 GB memory per vCPU) configurations. C4D instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
The N4 machine series is available on the Intel Emerald Rapids CPU platform and powered by Titanium. N4 machine types are optimized for flexibility and cost with both predefined and custom shapes and can scale up to 80 vCPUs at 640 GB of DDR5 memory. N4 is available in highcpu (2 GB per vCPU), standard (4 GB per vCPU), and highmem (8 GB per vCPU) configurations.
The N4D machine series is available on the AMD EPYC Turin CPU platform and powered by Titanium. N4D machine types are built for flexibility and cost optimization through an efficient architecture, and next generation dynamic resource management, making better use of resources on host machines. You can create N4D VMs using predefined machine types with up to 96 vCPUs and 768 GB of DDR5 memory, or you can create N4D VMs using custom machine types that allow you to choose varied combinations of compute and memory to optimize costs and reduce resource waste. N4D is available in highcpu (2 GB per vCPU), standard (4 GB per vCPU), and highmem (8 GB per vCPU) configurations.
The N2 machine series has up to 128 vCPUs, 8 GB of memory per vCPU, and is available on the Intel Ice Lake and Intel Cascade Lake CPU platforms.
The N2D machine series has up to 224 vCPUs, 8 GB of memory per vCPU, and is available on the third generation AMD EPYC Milan platform.
The C3 machine series offers up to 176 vCPUs and 2, 4, or 8 GB of memory per vCPU on the Intel Sapphire Rapids CPU platform and Titanium. C3 instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
The C3D machine series offers up to 360 vCPUs and 2, 4, or 8 GB of memory per vCPU on the AMD EPYC Genoa CPU platform and Titanium. C3D instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
The E2 machine series has up to 32 virtual cores (vCPUs) with up to 128 GB of memory with a maximum of 8 GB per vCPU, and the lowest cost of all machine series. The E2 machine series has a predefined CPU platform, running either an Intel processor or an AMD processor. The processor is selected for you when you create the instance. This machine series provides a variety of compute resources for the lowest price on Compute Engine, especially when paired with committed use discounts.
The Tau T2D machine series provides an optimized feature set for scaling out. Each VM instance can have up to 60 vCPUs, 4 GB of memory per vCPU, and is available on third generation AMD EPYC Milan processors. The Tau T2D machine series doesn't use cluster-threading, so a vCPU is equivalent to an entire core.
The N1 machine series VMs can have up to 96 vCPUs, up to 6.5 GB of memory per vCPU, and are available on Intel Sandy Bridge, Ivy Bridge, Haswell, Broadwell, and Skylake CPU platforms.
Arm
The N4A machine series is powered by Google's custom-designed Axion processor. The Axion process is built on Arm Neoverse N3 compute core, which supports Arm V9.2 architecture. The N4A machine series uses Titanium for CPU offloading. N4A instances provide up to 64 vCPUs with up to 8 GB of memory per vCPU with Uniform Memory Access (UMA) domain. N4A instances don't use simultaneous multithreading (SMT). A vCPU in a N4A instance is equivalent to an entire physical core. The N4A machine series is engineered to be our most efficient and flexible Arm-based series, delivering exceptional price-performance for a wide range of general-purpose and scale-out workloads. Ideal use cases include web and application servers, microservices, containerized applications using Google Kubernetes Engine (GKE), open-source databases, and development and testing environments.
The C4A machine series is powered by Google Axion, and built on Arm Neoverse V2 compute core, which supports Arm V9 architecture. C4A instances are powered by Titanium IPU with disk and network offloads, this improves instance performance by reducing on-host processing. C4A instances provide up to 72 vCPUs with up to 8 GB of memory per vCPU in a single UMA domain. C4A offers -lssd machine types that come with up to 6 TiB of Titanium SSD capacity. C4A bare metal instances (Preview) have 96 vCPUs and 768 GB of memory. C4A instances don't use simultaneous multithreading (SMT). A vCPU in a C4A instance is equivalent to an entire physical core.
The Tau T2A machine series is the first machine series in Google Cloud built on Arm Neoverse N1 core compute. Tau T2A machines are optimized to deliver compelling price for performance. Each VM can have up to 48 vCPUs with 4 GB of memory per vCPU. The Tau T2A machine series runs on a 64 core Ampere Altra processor with an Arm instruction set and an all-core frequency of 3 GHz. Tau T2A machine types support a single NUMA node and a vCPU is equivalent to an entire core.
Storage-optimized machine family guide
The storage-optimized machine family is best suited for high-performance and flash-optimized workloads such as SQL, NoSQL, and vector databases, scale-out data analytics, data warehouses and search, and distributed file systems that need fast access to large amounts of data stored in local storage. The storage-optimized machine family is designed to provide high local storage throughput and IOPS at sub-millisecond latency.
Z3 standardlssd instances can have up to 176 vCPUs, 1,408 GB of memory, and 36 TiB of Titanium SSD.
Z3 highlssd instances can have up to 88 vCPUs, 704 GB of memory, and 36 TiB of Titanium SSD.
Z3 bare metal instances have 192 vCPUs, 1,536 GB of memory, and 72 TiB of local Titanium SSD.
Z3 runs on the Intel Xeon Scalable processor (code name Sapphire Rapids) with DDR5 memory and Titanium offload processors. Z3 brings together compute, networking, and storage innovations into one platform. Z3 instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
Compute-optimized machine family guide
The compute-optimized machine family is optimized for running high performance computing (HPC), multi-node, and compute-bound applications by providing high performance per core.
H4D instances offer 192 vCPUs and 720 GB of DDR5 memory. H4D instances run on the AMD EPYC Turin CPU platform, with Titanium offload and Cloud RDMA support. H4D instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance. H4D delivers improved scalability for multi-node workloads and HPC workloads. Cloud RDMA is a networking infrastructure component that lets you build a true cloud HPC platform that can run scientific computations and ML/AI workloads. Cloud RDMA delivers price performance ratios comparable to on-premise infrastructure.
H3 instances offer 88 vCPUs and 352 GB of DDR5 memory. H3 instances run on the Intel Sapphire Rapids CPU platform and Titanium offload processors. H3 instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance. H3 delivers performance improvements for a wide variety of HPC workloads such as molecular dynamics, computational geoscience, financial risk analysis, weather modeling, frontend and backend EDA, and computational fluid dynamics.
C2 instances offer up to 60 vCPUs, 4 GB of memory per vCPU, and are available on the Intel Cascade Lake CPU platform. C2 instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
C2D instances offer up to 112 vCPUs, up to 8 GB of memory per vCPU, and are available on the third generation AMD EPYC Milan platform. C2D instances are aligned with the underlying NUMA architecture to offer optimal, reliable, and consistent performance.
Memory-optimized machine family guide
The memory-optimized machine family has machine series that are ideal for OLAP and OLTP SAP workloads, genomic modeling, electronic design automation, and memory intensive HPC workloads. This family offers more memory per core than any other machine family, with up to 32 TB of memory.
X4 bare metal instances offer up to 1,920 vCPUs, with either 12.8 or 17 GB of memory per vCPU. X4 has machine types with 6, 8, 12, 16, 24, and 32 TB of memory, and is available on the Intel Sapphire Rapids CPU platform.
M4 instances offer up to 224 vCPUs, with up to 26.5 GB of memory per vCPU, and are available on the Intel Emerald Rapids CPU platform.
M3 instances offer up to 128 vCPUs, with up to 30.5 GB of memory per vCPU, and are available on the Intel Ice Lake CPU platform.
M2 instances are available as 6 TB, 9 TB, and 12 TB machine types, and are available on the Intel Cascade Lake CPU platform.
M1 instances offer up to 160 vCPUs, 14.9 GB to 24 GB of memory per vCPU, and are available on the Intel Skylake and Broadwell CPU platforms.
Accelerator-optimized machine family guide
The accelerator-optimized machine family is ideal for massively parallelized Compute Unified Device Architecture (CUDA) compute workloads, such as machine learning (ML) and high performance computing (HPC). This machine family is the optimal choice for workloads that require GPUs.
Google also offers AI Hypercomputer for creating clusters of accelerator-optimized VMs with inter-GPU communication, which are designed for running very intensive AI and ML workloads. For more information, see AI Hypercomputer overview.
Arm
A4X Max bare metal instances offer up to 144 vCPUs and up to 960 GB of memory. Each A4X Max machine type has 4 NVIDIA B300 GPUs attached to 2 NVIDIA Grace CPUs. A4X Max bare metal instances have a maximum network bandwidth of up to 3,600 Gbps.
A4X instances offer up to 140 vCPUs and up to 884 GB of memory. Each A4X machine type has 4 NVIDIA B200 GPUs attached to 2 NVIDIA Grace CPUs. A4X instances have a maximum network bandwidth of up to 2,000 Gbps.
Important: The Compute Engine Service Level Agreement (SLA) doesn't apply to the A4X Max and A4X machine types.
x86
A4 instances offer up to 224 vCPUs and up to 3,968 GB of memory. Each A4 machine type has 8 NVIDIA B200 GPUs attached. A4 instances have a maximum network bandwidth of up to 3,600 Gbps and are available on the Intel Emerald Rapids CPU platform.
A3 instances offer up to 224 vCPUs and up to 2,952 GB of memory. Each A3 machine type has either 1, 2, 4, or 8 NVIDIA H100 or 8 H200 GPUs attached. A3 instances have a maximum network bandwidth of up to 3,200 Gbps and are available on the following CPU platforms:
Intel Emerald Rapids - A3 Ultra
Intel Sapphire Rapids - A3 Mega, High, and Edge
A3 instances are available with the A3 Edge machine type ( a3-edgegpu-8g-nolssd ), which offers 208 vCPUs, 1,872 GB of memory, and 8 NVIDIA H100 GPUs, on the Intel Sapphire Rapids CPU platform and Titanium.
A2 instances offer 12 to 96 vCPUs, and up to 1,360 GB of memory. Each A2 machine type has either 1, 2, 4, 8, or 16 NVIDIA A100 GPUs attached. A2 instances have a maximum network bandwidth of up to 100 Gbps and are available on the Intel Cascade Lake CPU platform.
G4 instances offer 6 to 384 vCPUs and up to 1,440 GB of memory. Each G4 instance has NVIDIA RTX PRO 6000 GPUs attached as follows:
Whole GPUs in quantities of 1, 2, 4, or 8
Fractional GPUs in quantities of 1/8, 1/4, or 1/2
G4 instances have a maximum network bandwidth of up to 400 Gbps and are available on the AMD EPYC Turin CPU platform.
G2 instances offer 4 to 96 vCPUs and up to 432 GB of memory. Each G2 machine type has either 1, 2, 4, or 8 NVIDIA L4 GPUs attached. G2 instances have a maximum network bandwidth of up to 100 Gbps and are available on the Intel Cascade Lake CPU platform.
Machine series comparison
Use the following table to compare each machine family and determine which one is appropriate for your workload. If, after reviewing this section, you are still unsure which family is best for your workload, start with the general-purpose machine family. For details about all supported processors, see CPU platforms.
To learn how your selection affects the performance of disk volumes attached to your compute instances, see:
Persistent Disk: Disk performance by machine type and vCPU count
Google Cloud Hyperdisk: Hyperdisk performance limits
Compare the characteristics of different machine series, from C4 to G2. You can select specific properties in the Choose instance properties to compare field to compare those properties across all machine series in the following table.
Workload type
Instance type
CPU type
Architecture
vCPUs
vCPU definition
Memory
Shared memory architecture
Custom machine types
Extended memory
Sole tenancy
Nested virtualization
Confidential Computing
Disk interface type
Hyperdisk Balanced
Hyperdisk Balanced HA
Hyperdisk Extreme
Hyperdisk ML
Hyperdisk Throughput
Local SSD
Max Local SSD
Standard PD
Balanced PD
SSD PD
Extreme PD
Network interfaces
Network performance
Tier_1 networking
Max GPUs
Sustained use discounts
Resource-based committed use discounts (CUDs)
Compute flexible CUDs
Spot VM discounts
Select one or more options Choose instance properties to compare
Workload type
Instance type
CPU type
Architecture
vCPUs
vCPU definition
Memory
Shared memory architecture
Custom machine types
Extended memory
Sole tenancy
Nested virtualization
Confidential Computing
Disk interface type
Hyperdisk Balanced
Hyperdisk Balanced HA
Hyperdisk Extreme
Hyperdisk ML
Hyperdisk Throughput
Local SSD
Max Local SSD
Standard PD
Balanced PD
SSD PD
Extreme PD
Network interfaces
Network performance
Tier_1 networking
Max GPUs
Sustained use discounts
Resource-based committed use discounts (CUDs)
Compute flexible CUDs
Spot VM discounts
Clear all
GPUs and compute instances
GPUs are used to accelerate workloads, and are supported for A4X Max, A4X, A4, A3, A2, G4, G2, and N1 instances. For instances that use A4X Max, A4X, A4, A3, A2, G4, or G2 machine types, the GPUs are automatically attached when you create the instance. For instances that use N1 machine types, you can attach GPUs to the instance during or after instance creation. GPUs can't be used with any other machine series.
Accelerator-optimized instances have a fixed number of GPUs, vCPUs and memory per machine type, with the exception of G2 machines that offer a custom memory range. N1 instances with fewer GPUs attached are limited to a maximum number of vCPUs. In general, a higher number of GPUs lets you create instances with a higher number of vCPUs and memory.
For more information, see GPUs on Compute Engine.
What's next
Learn how to create and start a VM.
Learn how to create a VM with a custom machine type.
Complete the Quickstart using a Linux VM.
Complete the Quickstart using a Windows VM.
Learn more about attaching block storage to your VMs.
Was this helpful?
Send feedback
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-05-08 UTC.
Products and pricing
See all products
Google Cloud pricing
Google Cloud Marketplace
Contact sales
Support
Community forums
Support
Release Notes
System status
Resources
GitHub
Getting Started with Google Cloud
Code samples
Cloud Architecture Center
Training and Certification
Engage
Blog
Events
X (Twitter)
Google Cloud on YouTube
Google Cloud Tech on YouTube
About Google
Privacy
Site terms
Google Cloud terms
Manage cookies
Our third decade of climate action: join us
Sign up for the Google Cloud newsletter Subscribe
Language
English
Deutsch
Español
Español – América Latina
Français
Indonesia
Italiano
Português
Português – Brasil
עברית
中文 – 简体
中文 – 繁體
日本語
한국어
