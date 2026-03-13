# src/scraper.py - Manual scheme data

import os
import pandas as pd
from pathlib import Path

SCHEMES = [
    {
        "scheme_name": "PM-KISAN",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "content": """SCHEME NAME: PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Agriculture
STATE: Central Government

DESCRIPTION:
PM-KISAN is a Central Sector scheme launched in February 2019. It provides income support of Rs. 6000 per year to all land holding farmer families across the country. The amount is paid in three equal installments of Rs. 2000 every four months directly into the bank accounts of farmers through Direct Benefit Transfer (DBT).

BENEFITS:
- Financial assistance of Rs. 6,000 per year
- Paid in 3 installments of Rs. 2,000 each
- Direct transfer to bank account
- No middlemen involved

ELIGIBILITY:
- All land holding farmer families with cultivable land
- Both husband and wife can be considered one family unit
- Small and marginal farmers are prioritized
- Farmer must be an Indian citizen
- Must have valid Aadhaar card
- Must have a bank account linked to Aadhaar

WHO IS NOT ELIGIBLE:
- Institutional land holders
- Farmer families holding constitutional posts
- Former and present Ministers, MPs, MLAs
- Government employees (except Multi Tasking Staff/Class IV)
- Income tax payers
- Professionals like doctors, engineers, lawyers, CAs

HOW TO APPLY:
1. Visit the official PM-KISAN portal: pmkisan.gov.in
2. Click on Farmers Corner
3. Click on New Farmer Registration
4. Enter Aadhaar number and select state
5. Fill in all required details
6. Submit the form
7. You can also register through Common Service Centres (CSC)
8. State/UT governments and district level officers also facilitate registration

DOCUMENTS REQUIRED:
- Aadhaar Card (mandatory)
- Bank account details
- Land ownership documents
- Citizenship proof

OFFICIAL WEBSITE: pmkisan.gov.in
HELPLINE: 155261 / 011-24300606"""
    },
    {
        "scheme_name": "AYUSHMAN-BHARAT-PMJAY",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "content": """SCHEME NAME: Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)
MINISTRY: Ministry of Health and Family Welfare
CATEGORY: Health Insurance
STATE: Central Government

DESCRIPTION:
Ayushman Bharat PM-JAY is the world's largest health insurance scheme launched in September 2018. It provides health coverage of Rs. 5 lakh per family per year for secondary and tertiary care hospitalization. The scheme covers over 10 crore poor and vulnerable families.

BENEFITS:
- Health coverage of Rs. 5 lakh per family per year
- Cashless and paperless treatment at empanelled hospitals
- Covers pre and post hospitalization expenses
- No restriction on family size or age
- Covers 1,949 medical procedures
- Covers all pre-existing diseases from day one
- Transport allowance also provided

ELIGIBILITY:
- Families listed in Socio Economic Caste Census (SECC) 2011 data
- All enrolled families under Rashtriya Swasthya Bima Yojana (RSBY)
- No income limit - based on deprivation criteria

HOW TO CHECK ELIGIBILITY:
1. Visit pmjay.gov.in
2. Click Am I Eligible
3. Enter mobile number and OTP
4. Search by name, HHD number, ration card, or mobile number

HOW TO APPLY:
- No registration needed if already in SECC database
- Visit nearest Common Service Centre or empanelled hospital
- Carry Aadhaar card or ration card for verification
- Ayushman card will be issued at the hospital

DOCUMENTS REQUIRED:
- Aadhaar Card
- Ration Card
- Any government ID proof

OFFICIAL WEBSITE: pmjay.gov.in
HELPLINE: 14555"""
    },
    {
        "scheme_name": "PM-AWAS-YOJANA-URBAN",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Housing",
        "content": """SCHEME NAME: Pradhan Mantri Awas Yojana - Urban (PMAY-U)
MINISTRY: Ministry of Housing and Urban Affairs
CATEGORY: Housing
STATE: Central Government

DESCRIPTION:
PMAY-Urban aims to provide housing for all in urban areas. The scheme provides central assistance to Urban Local Bodies for providing houses to all eligible urban households.

BENEFITS:
- Interest subsidy on home loans
- EWS/LIG: 6.5% interest subsidy for loan up to Rs. 6 lakh
- MIG-I: 4% interest subsidy for loan up to Rs. 9 lakh
- MIG-II: 3% interest subsidy for loan up to Rs. 12 lakh
- Direct grant for house construction under BLC component

ELIGIBILITY:
- EWS: Annual household income up to Rs. 3 lakh
- LIG: Annual household income Rs. 3-6 lakh
- MIG-I: Annual household income Rs. 6-12 lakh
- MIG-II: Annual household income Rs. 12-18 lakh
- Beneficiary family should not own a pucca house anywhere in India

HOW TO APPLY:
1. Visit pmaymis.gov.in
2. Click on Citizen Assessment
3. Select the appropriate category
4. Enter Aadhaar number
5. Fill in all personal and income details
6. Submit the application

DOCUMENTS REQUIRED:
- Aadhaar Card
- Income certificate
- Bank account details
- Property documents if applicable

OFFICIAL WEBSITE: pmaymis.gov.in
HELPLINE: 1800-11-6446"""
    },
    {
        "scheme_name": "MUDRA-YOJANA",
        "ministry": "Ministry of Finance",
        "category": "Finance and Banking",
        "content": """SCHEME NAME: Pradhan Mantri MUDRA Yojana (PMMY)
MINISTRY: Ministry of Finance
CATEGORY: Finance / Entrepreneurship
STATE: Central Government

DESCRIPTION:
MUDRA Yojana was launched in April 2015 to provide loans up to Rs. 10 lakh to non-corporate, non-farm small and micro enterprises. The scheme helps small businesses get formal credit without collateral.

BENEFITS:
Three categories of loans:
- Shishu: Loans up to Rs. 50,000
- Kishore: Loans from Rs. 50,001 to Rs. 5 lakh
- Tarun: Loans from Rs. 5 lakh to Rs. 10 lakh
- No collateral required
- Mudra Card provided for working capital needs

ELIGIBILITY:
- Any Indian citizen with a business plan for non-farm income generating activity
- Small manufacturers, shopkeepers, fruit/vegetable vendors
- Artisans, food service units, repair shops

HOW TO APPLY:
1. Prepare a business plan
2. Approach any bank, MFI, or NBFC
3. Fill Mudra loan application form
4. Submit required documents
5. Can also apply online at udyamimitra.in

DOCUMENTS REQUIRED:
- Identity proof (Aadhaar/PAN)
- Address proof
- Business plan / project report
- Bank statements last 6 months

OFFICIAL WEBSITE: mudra.org.in"""
    },
    {
        "scheme_name": "NREGA-MGNREGS",
        "ministry": "Ministry of Rural Development",
        "category": "Employment",
        "content": """SCHEME NAME: Mahatma Gandhi National Rural Employment Guarantee Scheme (MGNREGS)
MINISTRY: Ministry of Rural Development
CATEGORY: Employment / Rural Development
STATE: Central Government

DESCRIPTION:
MGNREGS provides at least 100 days of guaranteed wage employment in a financial year to every household in rural areas whose adult members volunteer to do unskilled manual work.

BENEFITS:
- Minimum 100 days of wage employment per household per year
- Wages paid at statutory minimum wage rates
- Payment directly into bank/post office accounts
- Work provided within 5 km of residence
- If work not provided within 15 days, unemployment allowance paid

ELIGIBILITY:
- Rural households
- Adult members 18 years and above
- Willing to do unskilled manual work
- Must be a resident of the Gram Panchayat area

HOW TO APPLY:
1. Visit your local Gram Panchayat office
2. Register household by submitting application with family details
3. Job Card will be issued within 15 days
4. Submit written application for work
5. Work will be provided within 15 days of application

DOCUMENTS REQUIRED:
- Proof of residence
- Age proof for adult members
- Photograph of all adult members
- Bank account details

OFFICIAL WEBSITE: nrega.nic.in
HELPLINE: 1800-111-555"""
    },
    {
        "scheme_name": "PMJJBY-LIFE-INSURANCE",
        "ministry": "Ministry of Finance",
        "category": "Insurance",
        "content": """SCHEME NAME: Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)
MINISTRY: Ministry of Finance
CATEGORY: Life Insurance
STATE: Central Government

DESCRIPTION:
PMJJBY is a government-backed life insurance scheme for people between 18 and 50 years with bank accounts. It offers renewable one-year life cover of Rs. 2 lakh at Rs. 436 per year.

BENEFITS:
- Life insurance cover of Rs. 2 lakh
- Premium: Rs. 436 per year auto-debited from bank account
- Cover period: 1st June to 31st May
- Death benefit for any cause of death

ELIGIBILITY:
- Age: 18 to 50 years
- Must have a savings bank account
- Must give consent for auto-debit of premium

HOW TO APPLY:
1. Visit your bank branch or insurance company
2. Fill the enrollment form
3. Give auto-debit consent
4. Premium of Rs. 436 will be auto-debited every year

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- Nomination details

OFFICIAL WEBSITE: jansuraksha.gov.in
HELPLINE: 1800-180-1111"""
    },
    {
        "scheme_name": "PMSBY-ACCIDENT-INSURANCE",
        "ministry": "Ministry of Finance",
        "category": "Insurance",
        "content": """SCHEME NAME: Pradhan Mantri Suraksha Bima Yojana (PMSBY)
MINISTRY: Ministry of Finance
CATEGORY: Accident Insurance
STATE: Central Government

DESCRIPTION:
PMSBY is a government-backed accident insurance scheme for people between 18 and 70 years at a premium of just Rs. 20 per year.

BENEFITS:
- Rs. 2 lakh for accidental death or permanent total disability
- Rs. 1 lakh for permanent partial disability
- Premium: only Rs. 20 per year
- Auto-debited from bank account in May each year

ELIGIBILITY:
- Age: 18 to 70 years
- Must have a savings bank account
- Must give consent for auto-debit

HOW TO APPLY:
1. Visit bank branch or use banking app
2. Fill enrollment/auto-debit consent form
3. Premium auto-debited on 1st June
4. Coverage valid from 1st June to 31st May

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details

OFFICIAL WEBSITE: jansuraksha.gov.in
HELPLINE: 1800-180-1111"""
    },
    {
        "scheme_name": "KISAN-CREDIT-CARD",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture / Finance",
        "content": """SCHEME NAME: Kisan Credit Card (KCC)
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Agriculture / Credit
STATE: Central Government

DESCRIPTION:
The Kisan Credit Card scheme provides farmers with affordable credit for agricultural needs. The scheme was revamped in 2019 to include fishermen and animal husbandry farmers.

BENEFITS:
- Credit limit based on land holding and crops
- Interest rate: 7% per annum effective 4% with subvention
- Flexible repayment tied to harvest season
- Personal accident insurance cover
- Covers fishermen and animal husbandry farmers too

ELIGIBILITY:
- All farmers including small, marginal, tenant farmers
- Oral lessees and sharecroppers
- Self Help Groups of farmers
- Fishermen with boat and license
- Animal husbandry farmers

HOW TO APPLY:
1. Visit nearest bank branch
2. Fill KCC application form
3. Submit land records and ID proof
4. Bank will assess credit limit based on land holding
5. KCC issued as ATM-cum-debit card

DOCUMENTS REQUIRED:
- Land records / ownership documents
- Identity proof Aadhaar/PAN
- Address proof
- Passport size photographs

OFFICIAL WEBSITE: pmkisan.gov.in/kcc"""
    },
    {
        "scheme_name": "STARTUP-INDIA",
        "ministry": "Ministry of Commerce and Industry",
        "category": "Entrepreneurship",
        "content": """SCHEME NAME: Startup India
MINISTRY: Ministry of Commerce and Industry
CATEGORY: Entrepreneurship / Innovation
STATE: Central Government

DESCRIPTION:
Startup India launched in January 2016 to build a strong ecosystem for nurturing innovation and startups in India.

BENEFITS:
- Income tax exemption for 3 years out of first 10 years
- Exemption from capital gains tax
- Rs. 10,000 crore Fund of Funds for startups
- Fast track patent examination at 80% rebate on fees
- Self-certification for 9 labor and environment laws
- Easy winding up within 90 days

ELIGIBILITY:
- Private Limited Company, LLP, or Registered Partnership
- Up to 10 years from date of incorporation
- Annual turnover not exceeding Rs. 100 crore
- Working towards innovation or improvement of products

HOW TO REGISTER:
1. Visit startupindia.gov.in
2. Register on the portal
3. Apply for DPIIT recognition
4. Upload required documents
5. Get recognized within 2 working days

DOCUMENTS REQUIRED:
- Certificate of Incorporation
- PAN of entity
- Brief about products/services

OFFICIAL WEBSITE: startupindia.gov.in"""
    },
    {
        "scheme_name": "SKILL-INDIA-PMKVY",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "category": "Skill Development",
        "content": """SCHEME NAME: Pradhan Mantri Kaushal Vikas Yojana (PMKVY) - Skill India
MINISTRY: Ministry of Skill Development and Entrepreneurship
CATEGORY: Skill Development / Employment
STATE: Central Government

DESCRIPTION:
PMKVY aims to enable Indian youth to take up industry-relevant skill training to help them secure better livelihoods.

BENEFITS:
- Free skill training short-term courses of 2 weeks to 3 months
- Monetary reward after certification Rs. 8,000 average
- Government-recognized certificate
- Placement assistance
- Training in over 300 job roles across 38 sectors

ELIGIBILITY:
- Indian nationals
- Unemployed youth and school/college dropouts
- Age: 15-45 years varies by sector
- No specific educational qualification required for most courses

HOW TO APPLY:
1. Visit pmkvyofficial.org or skillindiadigital.gov.in
2. Search for training centers near you
3. Register online or visit nearest PMKVY training center
4. Enroll in desired course
5. Complete training and appear for assessment
6. Receive certificate and reward amount

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- Educational certificates if any

OFFICIAL WEBSITE: pmkvyofficial.org
HELPLINE: 088000-55555"""
    },
    {
        "scheme_name": "NATIONAL-SCHOLARSHIP-PORTAL",
        "ministry": "Ministry of Electronics and IT",
        "category": "Education",
        "content": """SCHEME NAME: National Scholarship Portal (NSP)
MINISTRY: Multiple Ministries coordinated by MeitY
CATEGORY: Education / Scholarships
STATE: Central Government

DESCRIPTION:
The National Scholarship Portal is a one-stop platform hosting various scholarship schemes from Central Government, State Governments, and UGC/AICTE for SC, ST, OBC, minority communities and economically weaker sections.

KEY SCHOLARSHIPS:
1. Pre-Matric Scholarship for SC/ST/OBC students Class 1-10
2. Post-Matric Scholarship for SC/ST/OBC students Class 11 onwards
3. Merit-cum-Means Scholarship for Minorities
4. National Merit Scholarship
5. Central Sector Scholarship for College Students

BENEFITS:
- Financial assistance ranging from Rs. 1,000 to Rs. 20,000+ per year
- Directly credited to student bank accounts
- Covers tuition fees and maintenance allowance
- Renewable annually subject to performance

ELIGIBILITY:
- Indian citizens
- Family income below Rs. 2.5 lakh per year typically
- Must belong to eligible category SC/ST/OBC/Minority/EWS
- Must be studying in a recognized institution

HOW TO APPLY:
1. Visit scholarships.gov.in
2. Register as new student
3. Login and select applicable scholarship
4. Fill application form
5. Upload required documents
6. Submit before deadline usually October-November

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- Income certificate
- Caste/community certificate
- Previous year mark sheet
- Bonafide certificate from institution

OFFICIAL WEBSITE: scholarships.gov.in
HELPLINE: 0120-6619540"""
    },
    {
        "scheme_name": "STANDUP-INDIA",
        "ministry": "Ministry of Finance",
        "category": "Finance / Entrepreneurship",
        "content": """SCHEME NAME: Stand-Up India
MINISTRY: Ministry of Finance / SIDBI
CATEGORY: Entrepreneurship / Finance
STATE: Central Government

DESCRIPTION:
Stand-Up India launched in April 2016 facilitates bank loans between Rs. 10 lakh and Rs. 1 crore to SC/ST borrowers and women borrowers for setting up greenfield enterprises.

BENEFITS:
- Loans from Rs. 10 lakh to Rs. 1 crore
- For SC/ST and women entrepreneurs
- Composite loan term loan plus working capital
- Repayment period up to 7 years
- Moratorium period up to 18 months

ELIGIBILITY:
- SC or ST borrowers above 18 years
- Women entrepreneurs above 18 years
- For greenfield projects only
- Not in default to any bank/financial institution

HOW TO APPLY:
1. Visit standupmitra.in
2. Register on the portal
3. Apply online or visit any scheduled commercial bank branch
4. Submit business plan and required documents

DOCUMENTS REQUIRED:
- Identity proof Aadhaar/PAN
- Address proof
- Caste certificate for SC/ST
- Business plan / project report
- Last 6 months bank statement

OFFICIAL WEBSITE: standupmitra.in"""
    },
    {
        "scheme_name": "ATAL-PENSION-YOJANA",
        "ministry": "Ministry of Finance",
        "category": "Pension / Social Security",
        "content": """SCHEME NAME: Atal Pension Yojana (APY)
MINISTRY: Ministry of Finance / PFRDA
CATEGORY: Pension / Social Security
STATE: Central Government

DESCRIPTION:
Atal Pension Yojana is a government-backed pension scheme for unorganized sector workers providing guaranteed pension of Rs. 1,000 to Rs. 5,000 per month at age 60.

BENEFITS:
- Guaranteed pension of Rs. 1,000 to Rs. 5,000 per month
- Pension starts at age 60
- On death of subscriber, spouse gets same pension
- On death of both, nominee gets corpus amount

ELIGIBILITY:
- Indian citizens between 18 to 40 years
- Must have a savings bank account
- Must have mobile number linked to bank account
- Not an income tax payer for government co-contribution

HOW TO APPLY:
1. Visit any bank branch or post office
2. Fill APY registration form
3. Provide Aadhaar and mobile number
4. Choose pension amount Rs. 1,000 to 5,000
5. Auto-debit mandate will be set up

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- Mobile number

OFFICIAL WEBSITE: npscra.nsdl.co.in"""
    },
    {
        "scheme_name": "PM-FASAL-BIMA-YOJANA",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture / Insurance",
        "content": """SCHEME NAME: Pradhan Mantri Fasal Bima Yojana (PMFBY)
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Crop Insurance
STATE: Central Government

DESCRIPTION:
PMFBY provides comprehensive crop insurance coverage against non-preventable natural risks from pre-sowing to post-harvest stage.

BENEFITS:
- Very low premium rates:
  Kharif crops: 2% of sum insured
  Rabi crops: 1.5% of sum insured
  Annual commercial crops: 5%
- Covers losses from natural calamities, pests, diseases
- Covers post-harvest losses for 14 days
- Uses technology satellite and drones for quick settlement

ELIGIBILITY:
- All farmers growing notified crops in notified areas
- Compulsory for loanee farmers
- Voluntary for non-loanee farmers
- Both landowner and tenant farmers eligible

HOW TO APPLY:
- Loanee farmers: automatically enrolled through bank
- Non-loanee farmers visit nearest bank or CSC
- Fill PMFBY application form
- Pay premium before cut-off date
- Can also apply on pmfby.gov.in

DOCUMENTS REQUIRED:
- Land records / sowing certificate
- Bank account details
- Aadhaar Card

OFFICIAL WEBSITE: pmfby.gov.in
HELPLINE: 14447"""
    },
    {
        "scheme_name": "PMEGP-ENTREPRENEURSHIP",
        "ministry": "Ministry of MSME",
        "category": "Entrepreneurship / Employment",
        "content": """SCHEME NAME: Prime Minister Employment Generation Programme (PMEGP)
MINISTRY: Ministry of Micro Small and Medium Enterprises
CATEGORY: Entrepreneurship / Self Employment
STATE: Central Government

DESCRIPTION:
PMEGP is a credit-linked subsidy programme for generating employment through establishment of micro-enterprises in rural and urban areas.

BENEFITS:
- Subsidy 15-35% of project cost:
  General category urban: 15%
  General category rural: 25%
  Special category SC/ST/OBC/Women urban: 25%
  Special category rural: 35%
- Maximum project cost: Rs. 50 lakh manufacturing, Rs. 20 lakh service
- No collateral for loans up to Rs. 10 lakh

ELIGIBILITY:
- Any individual above 18 years
- Minimum 8th pass for projects above Rs. 10 lakh manufacturing
- Self Help Groups, charitable trusts also eligible
- Existing units not eligible

HOW TO APPLY:
1. Visit kviconline.gov.in
2. Register as applicant
3. Fill online application with project details
4. Select bank and submit
5. Complete EDP training before loan disbursement

DOCUMENTS REQUIRED:
- Project report
- Identity and address proof
- Educational certificates
- Caste certificate if applicable

OFFICIAL WEBSITE: kviconline.gov.in/pmegp"""
    },
    {
        "scheme_name": "PM-SVANidhi",
        "ministry": "Ministry of Housing and Urban Affairs",
        "category": "Finance / Urban",
        "content": """SCHEME NAME: PM Street Vendor's AtmaNirbhar Nidhi (PM SVANidhi)
MINISTRY: Ministry of Housing and Urban Affairs
CATEGORY: Finance / Urban Development
STATE: Central Government

DESCRIPTION:
PM SVANidhi is a micro-credit scheme launched in June 2020 to provide affordable loans to street vendors affected by COVID-19 lockdown. It helps vendors resume their livelihoods and become self-reliant.

BENEFITS:
- Initial loan of Rs. 10,000 without collateral
- On timely repayment, eligible for Rs. 20,000 loan
- Further eligible for Rs. 50,000 loan
- Interest subsidy of 7% per annum
- Digital transaction incentive of Rs. 1,200 per year
- No penalty for early repayment

ELIGIBILITY:
- Street vendors vending in urban areas as on or before March 24, 2020
- Vendors with Certificate of Vending issued by Urban Local Bodies
- Vendors identified in survey but not issued certificate
- Vendors with letter of recommendation from Urban Local Body

HOW TO APPLY:
1. Visit nearest bank, MFI, or SHG
2. Can also apply online at pmsvanidhi.mohua.gov.in
3. Fill application form with required details
4. Submit vending certificate or ULB recommendation
5. Loan disbursed within 30 days

DOCUMENTS REQUIRED:
- Aadhaar Card
- Vending Certificate or ULB letter
- Bank account details
- Passport size photograph

OFFICIAL WEBSITE: pmsvanidhi.mohua.gov.in
HELPLINE: 1800-11-1979"""
    },
    {
        "scheme_name": "SUKANYA-SAMRIDHI-YOJANA",
        "ministry": "Ministry of Finance",
        "category": "Finance / Girl Child",
        "content": """SCHEME NAME: Sukanya Samridhi Yojana (SSY)
MINISTRY: Ministry of Finance
CATEGORY: Savings / Girl Child Welfare
STATE: Central Government

DESCRIPTION:
Sukanya Samridhi Yojana is a small deposit scheme for girl children launched as part of Beti Bachao Beti Padhao campaign. It offers one of the highest interest rates among government savings schemes.

BENEFITS:
- Interest rate: 8.2% per annum (revised quarterly)
- Tax exemption under Section 80C up to Rs. 1.5 lakh
- Maturity amount fully tax-free
- Partial withdrawal allowed after girl turns 18
- Account matures after 21 years from opening

ELIGIBILITY:
- Girl child below 10 years of age
- Only one account per girl child
- Maximum two accounts per family (three for twins/triplets)
- Must be Indian citizen

HOW TO APPLY:
1. Visit nearest post office or authorized bank
2. Fill SSY account opening form
3. Submit required documents
4. Minimum deposit of Rs. 250 to open account
5. Minimum Rs. 250, maximum Rs. 1.5 lakh per year

DOCUMENTS REQUIRED:
- Birth certificate of girl child
- Identity proof of parent/guardian
- Address proof of parent/guardian
- Photograph of parent/guardian

OFFICIAL WEBSITE: nsiindia.gov.in"""
    },
    {
        "scheme_name": "BETI-BACHAO-BETI-PADHAO",
        "ministry": "Ministry of Women and Child Development",
        "category": "Women / Girl Child",
        "content": """SCHEME NAME: Beti Bachao Beti Padhao (BBBP)
MINISTRY: Ministry of Women and Child Development
CATEGORY: Women Empowerment / Girl Child
STATE: Central Government

DESCRIPTION:
Beti Bachao Beti Padhao scheme was launched in January 2015 to address declining Child Sex Ratio and promote welfare of girl children through education and empowerment.

BENEFITS:
- Scholarships for girl students
- Awareness campaigns against female foeticide
- Education support for girls
- Vocational training for adolescent girls
- Financial incentives for girl child education
- Support for enrollment and retention of girls in schools

ELIGIBILITY:
- All girl children
- Focus on districts with low Child Sex Ratio
- All families with girl children
- Adolescent girls for Kishori Shakti Yojana component

HOW TO ACCESS:
1. Contact nearest Anganwadi center
2. Visit district Women and Child Development office
3. Approach nearest government school
4. Contact ASHA workers in rural areas

OFFICIAL WEBSITE: wcd.nic.in
HELPLINE: 181 (Women Helpline)"""
    },
    {
        "scheme_name": "UJJWALA-YOJANA",
        "ministry": "Ministry of Petroleum and Natural Gas",
        "category": "Energy / Women",
        "content": """SCHEME NAME: Pradhan Mantri Ujjwala Yojana (PMUY)
MINISTRY: Ministry of Petroleum and Natural Gas
CATEGORY: Energy / Women Empowerment
STATE: Central Government

DESCRIPTION:
PM Ujjwala Yojana provides free LPG connections to women from Below Poverty Line households to replace unhealthy cooking fuels and improve health of rural women.

BENEFITS:
- Free LPG connection with stove and first refill
- Financial assistance of Rs. 1,600 per connection
- EMI facility for purchasing stove and first refill
- First refill and hotplate free under PMUY 2.0
- Available to migrants without permanent address proof

ELIGIBILITY:
- Women above 18 years from BPL households
- Not already having LPG connection in household
- SECC-2011 listed households
- SC/ST households
- PM Awas Yojana (Gramin) beneficiaries
- Tea garden workers, forest dwellers, river islands

HOW TO APPLY:
1. Visit nearest LPG distributor
2. Fill KYC form
3. Submit Aadhaar and BPL/ration card
4. Connection released within 7 days

DOCUMENTS REQUIRED:
- Aadhaar Card
- BPL ration card or SECC data
- Bank account details
- Address proof

OFFICIAL WEBSITE: pmuy.gov.in
HELPLINE: 1800-233-3555"""
    },
    {
        "scheme_name": "JAL-JEEVAN-MISSION",
        "ministry": "Ministry of Jal Shakti",
        "category": "Water / Rural Development",
        "content": """SCHEME NAME: Jal Jeevan Mission (JJM)
MINISTRY: Ministry of Jal Shakti
CATEGORY: Water Supply / Rural Development
STATE: Central Government

DESCRIPTION:
Jal Jeevan Mission aims to provide safe and adequate drinking water through individual household tap connections to all households in rural India by 2024.

BENEFITS:
- Tap water connection to every rural household
- Minimum 55 litres per person per day
- Clean piped water at household level
- Employment during infrastructure creation
- Improved health outcomes

ELIGIBILITY:
- All rural households without piped water connection
- Priority to SC/ST households, JJM habitations
- Schools and Anganwadi centers also covered

HOW TO ACCESS:
- Implemented by State Governments
- Village Water and Sanitation Committee manages local infrastructure
- Contact Gram Panchayat or Block Development Officer
- Beneficiary households contribute to O&M

OFFICIAL WEBSITE: jaljeevanmission.gov.in
HELPLINE: 1916"""
    },
    {
        "scheme_name": "PMGDISHA-DIGITAL-LITERACY",
        "ministry": "Ministry of Electronics and IT",
        "category": "Education / Digital",
        "content": """SCHEME NAME: Pradhan Mantri Gramin Digital Saksharta Abhiyan (PMGDISHA)
MINISTRY: Ministry of Electronics and Information Technology
CATEGORY: Digital Literacy / Education
STATE: Central Government

DESCRIPTION:
PMGDISHA aims to make six crore rural households digitally literate by training one member per eligible household to use computers, smartphones, and the internet for daily tasks and government services.

BENEFITS:
- Free digital literacy training
- Government-recognized certificate
- Training in operating computers and smartphones
- Learning internet browsing and email
- Digital payments and online government services
- Social media awareness

ELIGIBILITY:
- Rural households
- One member per household
- Age: 14 to 60 years
- Priority to SC/ST, minorities, women, differently-abled, BPL

HOW TO APPLY:
1. Visit pmgdisha.in and register online
2. Contact nearest Common Service Centre
3. Visit Gram Panchayat office
4. Training conducted at local training centers
5. 20-hour training program over multiple sessions

DOCUMENTS REQUIRED:
- Aadhaar Card
- Proof of rural residence

OFFICIAL WEBSITE: pmgdisha.in"""
    },
    {
        "scheme_name": "AYUSHMAN-BHARAT-HWC",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health",
        "content": """SCHEME NAME: Ayushman Bharat - Health and Wellness Centres (HWC)
MINISTRY: Ministry of Health and Family Welfare
CATEGORY: Primary Healthcare
STATE: Central Government

DESCRIPTION:
Ayushman Bharat Health and Wellness Centres transform sub-health centres and primary health centres into comprehensive primary health care providers offering free essential medicines and diagnostics.

BENEFITS:
- Free primary healthcare services
- Free essential medicines
- Free diagnostic services
- Teleconsultation services
- Maternal and child health services
- Mental health and palliative care
- Screening for NCDs like diabetes and cancer

ELIGIBILITY:
- All citizens can access HWC services for free
- No registration required
- Universal access regardless of income

HOW TO ACCESS:
- Visit nearest Health and Wellness Centre
- Located at sub-centre or primary health centre level
- Mitra (health worker) available for assistance
- Teleconsultation available for specialist advice

OFFICIAL WEBSITE: nhm.gov.in
HELPLINE: 104"""
    },
    {
        "scheme_name": "PM-VISHWAKARMA-YOJANA",
        "ministry": "Ministry of MSME",
        "category": "Skill Development / Artisans",
        "content": """SCHEME NAME: PM Vishwakarma Yojana
MINISTRY: Ministry of Micro Small and Medium Enterprises
CATEGORY: Artisan Support / Skill Development
STATE: Central Government

DESCRIPTION:
PM Vishwakarma Yojana launched in September 2023 provides end-to-end support to artisans and craftspeople who work with their hands and tools covering 18 traditional trades.

BENEFITS:
- Recognition as Vishwakarma with PM Vishwakarma certificate
- Skill training: 5-7 days basic plus 15 days advanced
- Stipend of Rs. 500 per day during training
- Toolkit incentive of Rs. 15,000
- Collateral-free loan: Rs. 1 lakh at 5% interest (first tranche)
- Second tranche: Rs. 2 lakh
- Digital transaction incentive
- Marketing support

ELIGIBLE TRADES:
Carpenter, Boat Maker, Armourer, Blacksmith, Hammer and Tool Kit Maker, Locksmith, Goldsmith, Potter, Sculptor, Cobbler, Mason, Basket/Mat/Broom Maker, Doll and Toy Maker, Barber, Garland Maker, Washerman, Tailor, Fishing Net Maker

ELIGIBILITY:
- Artisan or craftsperson working in one of 18 trades
- Minimum age 18 years
- Not availed MUDRA or PM SVANidhi in last 5 years

HOW TO APPLY:
1. Visit nearest Common Service Centre
2. Register on pmvishwakarma.gov.in
3. Biometric verification through CSC
4. Receive PM Vishwakarma certificate

OFFICIAL WEBSITE: pmvishwakarma.gov.in"""
    },
    {
        "scheme_name": "NATIONAL-PENSION-SYSTEM",
        "ministry": "Ministry of Finance",
        "category": "Pension / Retirement",
        "content": """SCHEME NAME: National Pension System (NPS)
MINISTRY: Ministry of Finance / PFRDA
CATEGORY: Pension / Retirement Savings
STATE: Central Government

DESCRIPTION:
National Pension System is a voluntary retirement savings scheme that allows subscribers to make defined contributions towards planned savings and secure future through reasonable market-based returns.

BENEFITS:
- Market-linked returns (historically 9-12% per annum)
- Tax benefit under Section 80C up to Rs. 1.5 lakh
- Additional tax benefit under 80CCD(1B) up to Rs. 50,000
- Employer contribution also tax-free under 80CCD(2)
- Partial withdrawal allowed after 3 years
- 60% lump sum tax-free on maturity

ELIGIBILITY:
- Indian citizens between 18-70 years
- NRIs also eligible
- Both salaried and self-employed can join

HOW TO APPLY:
1. Visit bank, post office, or Point of Presence (PoP)
2. Fill NPS registration form
3. Submit KYC documents
4. Get PRAN (Permanent Retirement Account Number)
5. Can also register online at enps.nsdl.com

DOCUMENTS REQUIRED:
- Aadhaar Card
- PAN Card
- Bank account details
- Photograph

OFFICIAL WEBSITE: npstrust.org.in
HELPLINE: 1800-110-708"""
    },
    {
        "scheme_name": "DEEN-DAYAL-UPADHYAYA-GRAMEEN",
        "ministry": "Ministry of Rural Development",
        "category": "Employment / Rural",
        "content": """SCHEME NAME: Deen Dayal Upadhyaya Grameen Kaushalya Yojana (DDU-GKY)
MINISTRY: Ministry of Rural Development
CATEGORY: Skill Development / Rural Employment
STATE: Central Government

DESCRIPTION:
DDU-GKY is a placement-linked skill training program for rural poor youth. It funds and promotes skill development leading to placement in formal sector jobs with regular wages.

BENEFITS:
- Free skill training in market-relevant trades
- Residential training with boarding and lodging
- Post-placement support for 12 months
- Wage of minimum Rs. 6,000 per month after placement
- Guaranteed placement in formal sector
- Migration support for out-of-state placements
- Social security benefits

ELIGIBILITY:
- Rural youth between 15-35 years
- Age limit 45 years for women and special groups
- From poor households (SECC data)
- Must have passed at least Class 5

HOW TO APPLY:
1. Contact nearest District Rural Development Agency
2. Visit ddugky.gov.in for training centers
3. Register through Gram Panchayat
4. Undergo selection process
5. Join training program

OFFICIAL WEBSITE: ddugky.gov.in
HELPLINE: 1800-180-6127"""
    },
    {
        "scheme_name": "PMAY-GRAMIN",
        "ministry": "Ministry of Rural Development",
        "category": "Housing / Rural",
        "content": """SCHEME NAME: Pradhan Mantri Awas Yojana - Gramin (PMAY-G)
MINISTRY: Ministry of Rural Development
CATEGORY: Rural Housing
STATE: Central Government

DESCRIPTION:
PMAY-Gramin aims to provide pucca houses with basic amenities to all houseless and those living in kutcha and dilapidated houses in rural areas by 2024.

BENEFITS:
- Rs. 1.20 lakh assistance in plains
- Rs. 1.30 lakh in hilly/difficult areas
- Toilet construction support under SBM
- MGNREGS wages for unskilled labor (90-95 days)
- Piped water connection under JJM
- Direct bank transfer to beneficiary

ELIGIBILITY:
- Based on SECC 2011 data
- Houseless families
- Families living in 0 or 1 room kutcha house
- SC/ST households
- Freed bonded laborers
- Families with no adult earning member

HOW TO APPLY:
- Beneficiary list based on SECC data
- Contact Gram Panchayat or Block Development Officer
- Verification done by Gram Sabha
- Can check status on pmayg.nic.in

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- Job Card (MGNREGS)

OFFICIAL WEBSITE: pmayg.nic.in
HELPLINE: 1800-11-6446"""
    },
    {
        "scheme_name": "SWACHH-BHARAT-MISSION",
        "ministry": "Ministry of Jal Shakti",
        "category": "Sanitation / Rural",
        "content": """SCHEME NAME: Swachh Bharat Mission - Gramin (SBM-G)
MINISTRY: Ministry of Jal Shakti
CATEGORY: Sanitation / Rural Development
STATE: Central Government

DESCRIPTION:
Swachh Bharat Mission aims to achieve Open Defecation Free India by constructing household toilets and promoting behavioral change for cleanliness and hygiene.

BENEFITS:
- Financial incentive of Rs. 12,000 for toilet construction
- Direct bank transfer to beneficiary
- Community sanitation complex support
- Solid and liquid waste management
- Greywater management support

ELIGIBILITY:
- All BPL households without toilet
- APL households in SC/ST category
- Small and marginal farmers
- Landless laborers with homestead land
- Physically handicapped persons
- Women-headed households

HOW TO APPLY:
1. Contact Gram Panchayat
2. Apply to Block Development Officer
3. Can also apply online at sbm.gov.in
4. Verification by Swachhagrahi
5. Incentive released after toilet construction verified

DOCUMENTS REQUIRED:
- Aadhaar Card
- Bank account details
- BPL certificate if applicable

OFFICIAL WEBSITE: sbm.gov.in
HELPLINE: 1969"""
    },
    {
        "scheme_name": "RASHTRIYA-KRISHI-VIKAS-YOJANA",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "content": """SCHEME NAME: Rashtriya Krishi Vikas Yojana (RKVY)
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Agriculture / Rural Development
STATE: Central Government

DESCRIPTION:
RKVY aims to achieve 4% annual growth in agriculture by incentivizing states to increase investment in agriculture and allied sectors through flexible funding for district and state level projects.

BENEFITS:
- Financial support for agriculture infrastructure
- Funding for farm mechanization
- Post-harvest management support
- Agri-entrepreneurship support
- Soil health management funding
- Horticulture development support
- Rs. 20 lakh to Rs. 2 crore for agri-startups

ELIGIBILITY:
- Farmers through State Government schemes
- Farmer Producer Organizations (FPOs)
- Agri-entrepreneurs under RAFTAAR component
- Agriculture graduates for startup support

HOW TO ACCESS:
1. Contact State Agriculture Department
2. Apply through District Agriculture Officer
3. For agri-startups visit rkvy.nic.in
4. FPOs can apply through NABARD

OFFICIAL WEBSITE: rkvy.nic.in"""
    },
    {
        "scheme_name": "PRADHAN-MANTRI-MATRU-VANDANA",
        "ministry": "Ministry of Women and Child Development",
        "category": "Women / Maternity",
        "content": """SCHEME NAME: Pradhan Mantri Matru Vandana Yojana (PMMVY)
MINISTRY: Ministry of Women and Child Development
CATEGORY: Maternity Benefit / Women
STATE: Central Government

DESCRIPTION:
PMMVY is a maternity benefit program providing cash incentives to pregnant and lactating women for the first living child to compensate for wage loss and improve health and nutrition.

BENEFITS:
- Rs. 5,000 cash incentive in three installments for first child
- Rs. 6,000 for second child if girl
- Installment 1: Rs. 1,000 after pregnancy registration
- Installment 2: Rs. 2,000 after 6 months of pregnancy
- Installment 3: Rs. 2,000 after child birth and registration

ELIGIBILITY:
- All pregnant and lactating women
- For first living child (second child if girl from 2022)
- Excluding central and state government employees
- Age 19 years and above

HOW TO APPLY:
1. Register at nearest Anganwadi Centre or health facility
2. Fill PMMVY form 1A for first installment
3. Submit within 150 days of Last Menstrual Period
4. Subsequent forms for other installments

DOCUMENTS REQUIRED:
- Aadhaar Card of mother and father
- Bank account details
- MCP card (Mother and Child Protection card)

OFFICIAL WEBSITE: wcd.nic.in/pmmvy
HELPLINE: 7998799804"""
    },
    {
        "scheme_name": "SOIL-HEALTH-CARD-SCHEME",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture",
        "content": """SCHEME NAME: Soil Health Card Scheme
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Agriculture
STATE: Central Government

DESCRIPTION:
The Soil Health Card Scheme provides farmers with Soil Health Cards containing crop-wise recommendations for nutrients and fertilizers for individual farms to improve productivity.

BENEFITS:
- Free soil testing
- Crop-wise fertilizer recommendations
- Guidance on micronutrient deficiencies
- Helps reduce fertilizer costs
- Improves crop yield
- Card issued every two years

ELIGIBILITY:
- All farmers across India
- Free service for all landholding farmers

HOW TO GET SOIL HEALTH CARD:
1. Contact nearest Agriculture Department office
2. Soil sample collected from your farm
3. Sample tested at soil testing laboratory
4. Card issued within 30 days
5. Can also check soilhealth.dac.gov.in

OFFICIAL WEBSITE: soilhealth.dac.gov.in"""
    },
    {
        "scheme_name": "PM-KISAN-MANDHAN-YOJANA",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "category": "Agriculture / Pension",
        "content": """SCHEME NAME: Pradhan Mantri Kisan Mandhan Yojana (PM-KMY)
MINISTRY: Ministry of Agriculture and Farmers Welfare
CATEGORY: Farmer Pension
STATE: Central Government

DESCRIPTION:
PM-KMY is a voluntary and contributory pension scheme for small and marginal farmers providing minimum assured pension of Rs. 3,000 per month after age 60.

BENEFITS:
- Minimum pension of Rs. 3,000 per month after age 60
- Government contributes equal amount to farmer's contribution
- Family pension of 50% (Rs. 1,500) to spouse on death
- If farmer dies before 60, spouse can continue or withdraw

ELIGIBILITY:
- Small and marginal farmers with up to 2 hectares land
- Age: 18-40 years at time of enrollment
- Not covered under NPS, ESIC, EPFO
- Not an income tax payer

CONTRIBUTION:
- Age 18: Rs. 55 per month
- Age 30: Rs. 110 per month
- Age 40: Rs. 200 per month
- Government contributes equal amount

HOW TO APPLY:
1. Visit nearest Common Service Centre with Aadhaar and bank passbook
2. Self-enroll at maandhan.in
3. Auto-debit from PM-KISAN installment also possible

OFFICIAL WEBSITE: maandhan.in
HELPLINE: 1800-267-6888"""
    },
    {
        "scheme_name": "NATIONAL-RURAL-LIVELIHOOD-MISSION",
        "ministry": "Ministry of Rural Development",
        "category": "Employment / Women",
        "content": """SCHEME NAME: Deendayal Antyodaya Yojana - National Rural Livelihoods Mission (DAY-NRLM)
MINISTRY: Ministry of Rural Development
CATEGORY: Rural Livelihoods / Women Empowerment
STATE: Central Government

DESCRIPTION:
DAY-NRLM aims to reduce poverty by building strong institutions of the poor especially women Self Help Groups and federations providing financial services and livelihoods.

BENEFITS:
- Self Help Group (SHG) formation support
- Revolving fund of Rs. 15,000 per SHG
- Community Investment Fund up to Rs. 2.5 lakh
- Bank linkage at 7% interest rate
- Skill training and placement support
- Access to government schemes and entitlements
- Digital financial inclusion

ELIGIBILITY:
- Rural poor women
- BPL and vulnerable households
- SC/ST households
- Women-headed households
- Persons with disabilities

HOW TO JOIN:
1. Contact nearest Anganwadi or Block office
2. Join or form a Self Help Group of 10-15 women
3. Meet regularly and save regularly
4. Contact District Mission Management Unit

OFFICIAL WEBSITE: aajeevika.gov.in
HELPLINE: 1800-180-6127"""
    },
    {
        "scheme_name": "ATAL-INNOVATION-MISSION",
        "ministry": "NITI Aayog",
        "category": "Innovation / Education",
        "content": """SCHEME NAME: Atal Innovation Mission (AIM)
MINISTRY: NITI Aayog
CATEGORY: Innovation / Entrepreneurship / Education
STATE: Central Government

DESCRIPTION:
Atal Innovation Mission is the Government's flagship initiative to promote innovation and entrepreneurship across the country through Atal Tinkering Labs, Atal Incubation Centres, and Atal Community Innovation Centres.

BENEFITS:
- Atal Tinkering Labs: Rs. 20 lakh grant for schools
- Atal Incubation Centres: Up to Rs. 10 crore for 5 years
- Atal Community Innovation Centres for rural innovation
- Mentorship and networking support
- Access to tools like 3D printers, robotics kits
- National competitions and recognition

ELIGIBILITY:
- Schools for Atal Tinkering Labs (Classes 6-12)
- Educational institutions for Atal Incubation Centres
- NGOs and community organizations for ACIC
- Startups and entrepreneurs for incubation

HOW TO APPLY:
1. Visit aim.gov.in
2. Apply online for relevant program
3. Schools can apply for ATL grants
4. Institutions apply for incubation centres

OFFICIAL WEBSITE: aim.gov.in"""
    },
    {
        "scheme_name": "NATIONAL-FOOD-SECURITY-ACT",
        "ministry": "Ministry of Consumer Affairs Food and Public Distribution",
        "category": "Food Security",
        "content": """SCHEME NAME: National Food Security Act (NFSA) - Public Distribution System
MINISTRY: Ministry of Consumer Affairs Food and Public Distribution
CATEGORY: Food Security
STATE: Central Government

DESCRIPTION:
The National Food Security Act ensures food and nutritional security by providing subsidized food grains to approximately two-thirds of India's population through the Targeted Public Distribution System.

BENEFITS:
- Priority households: 5 kg food grains per person per month
- Antyodaya households: 35 kg per family per month
- Rice at Rs. 3 per kg
- Wheat at Rs. 2 per kg
- Coarse grains at Rs. 1 per kg
- Pregnant women and lactating mothers entitled to free meals
- Children 6 months to 14 years entitled to free meals

ELIGIBILITY:
- Priority Households as identified by State Governments
- Antyodaya Anna Yojana households (poorest of poor)
- Pregnant women and lactating mothers
- Children up to 14 years

HOW TO GET RATION CARD:
1. Apply to nearest Food Supply Office
2. Submit income and residence proof
3. Ration card issued after verification
4. Can also apply online through State portals

DOCUMENTS REQUIRED:
- Identity proof
- Address proof
- Income certificate
- Family photograph

OFFICIAL WEBSITE: dfpd.gov.in
HELPLINE: 1967"""
    },
    {
        "scheme_name": "PRADHAN-MANTRI-SURAKSHIT-MATRITVA",
        "ministry": "Ministry of Health and Family Welfare",
        "category": "Health / Women",
        "content": """SCHEME NAME: Pradhan Mantri Surakshit Matritva Abhiyan (PMSMA)
MINISTRY: Ministry of Health and Family Welfare
CATEGORY: Maternal Health
STATE: Central Government

DESCRIPTION:
PMSMA provides fixed-day assured comprehensive and quality antenatal care to all pregnant women on the 9th of every month at government health facilities.

BENEFITS:
- Free antenatal checkup on 9th of every month
- Blood pressure and weight check
- Abdominal examination
- Blood and urine tests
- Ultrasound if needed
- Iron and folic acid supplements
- JSSK benefits for referral

ELIGIBILITY:
- All pregnant women in second and third trimester
- Free service at all government health facilities
- Private sector volunteers also participate

HOW TO ACCESS:
1. Visit nearest government health facility on 9th of month
2. No appointment needed
3. Carry MCP card
4. Available at PHC, CHC, District Hospital

OFFICIAL WEBSITE: pmsma.nhp.gov.in
HELPLINE: 104"""
    },
    {
        "scheme_name": "DIGITAL-INDIA",
        "ministry": "Ministry of Electronics and IT",
        "category": "Technology / Digital",
        "content": """SCHEME NAME: Digital India Programme
MINISTRY: Ministry of Electronics and Information Technology
CATEGORY: Technology / Digital Transformation
STATE: Central Government

DESCRIPTION:
Digital India is a flagship programme launched in July 2015 to transform India into a digitally empowered society and knowledge economy. It covers three key areas: digital infrastructure, digital services, and digital literacy.

BENEFITS:
- High speed internet in all gram panchayats
- Common Service Centres (CSC) in every village
- Digital Locker for storing documents online
- eSign service for digital signatures
- MyGov platform for citizen engagement
- UMANG app for all government services
- DigiMitra for last mile digital services
- National Scholarships Portal
- e-Hospital for online hospital services
- Unified Mobile Application for government services

KEY INITIATIVES:
- DigiLocker: Store and share documents digitally
- UMANG App: 1200+ government services on one app
- Bharat Net: Broadband to all gram panchayats
- Common Service Centres: 5 lakh+ centers nationwide
- India Stack: APIs for digital services
- CoWIN: Vaccination management platform

ELIGIBILITY:
- All Indian citizens
- All government services now available digitally
- No specific eligibility criteria

HOW TO ACCESS:
1. Visit digitalindia.gov.in
2. Download UMANG app
3. Register on DigiLocker at digilocker.gov.in
4. Visit nearest Common Service Centre
5. Use Aadhaar for digital authentication

OFFICIAL WEBSITE: digitalindia.gov.in"""
    },
]


def create_scheme_files():
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    print("Creating scheme data files...")

    for scheme in SCHEMES:
        filepath = f"data/processed/{scheme['scheme_name']}.txt"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(scheme["content"])
        print(f"  ✅ Created: {scheme['scheme_name']}.txt")

    df = pd.DataFrame([{
        "scheme_name": s["scheme_name"],
        "ministry": s["ministry"],
        "category": s["category"],
    } for s in SCHEMES])

    df.to_csv("data/metadata.csv", index=False)
    print(f"\n✅ Created {len(SCHEMES)} scheme files!")
    print(f"✅ Saved metadata.csv")


if __name__ == "__main__":
    create_scheme_files()