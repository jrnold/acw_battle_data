CREATE TABLE IF NOT EXISTS Category  (
	PK_ID INT PRIMARY KEY,
	CATEGORY VARCHAR(100),
	ABBR varchar(10),
	DESCRIPTION varchar(200),
	ISDELETE bit NOT NULL,
	PUBDATE datetime NOT NULL,
	UPDATEDATE datetime,
	UPDATEBY varchar(30),
	UPDATETYPE varchar(15),
	COMMENTS varchar(255)
	);

CREATE TABLE Cemeteries_Info(
	CT_IMAGE varchar(28) NULL,
	CT_GRAVENUMBER varchar(5) NULL,
	CT_LASTNAME varchar(20) NULL,
	CT_FIRSTNAME varchar(20) NULL,
	CT_RANK varchar(8) NULL,
	CT_COMPANY varchar(10) NULL,
	CT_STATE varchar(5) NULL,
	CT_BRANCHOFSERVICE varchar(20) NULL,
	CT_SIDE varchar(15) NULL,
	CT_TYPE varchar(15) NULL,
	CT_DATEOFDEATH varchar(20) NULL,
	CT_BURIALPLACE varchar(30) NULL,
	CT_RESEARCHCOMMENTS varchar(100) NULL,
	CT_PUBLICCOMMENTS varchar(100) NULL,
	CT_ENLISTAGE varchar(2) NULL,
	CT_ENLISTPLACE varchar(50) NULL,
	CT_ENLISTDATE varchar(20) NULL,
	CT_OCCUPATION varchar(25) NULL,
	CT_RESIDENCE varchar(50) NULL,
	CT_UNITNAME varchar(70) NULL,
	CT_REGT varchar(40) NULL,
	CT_ISDELETE bit NOT NULL,
	CT_PUBDATE datetime NOT NULL,
	CT_UPDATEDATE datetime NULL,
	CT_UPDATEBY int NULL,
	CT_UPDATETYPE varchar(15) NULL,
	CT_COMMENTS varchar(255) NULL,
	CT_ID int PRIMARY KEY
	);

CREATE TABLE Cemeteries_Info_unusedColumns(
	CT_BLOCK varchar(5) NULL,
	CT_STONESHOWS varchar(115) NULL,
	CT_BREMER varchar(1) NULL,
	CT_REGISTER varchar(1) NULL,
	CT_DONE varchar(1) NULL,
	CT_TYPEOFSTONE varchar(6) NULL,
	CT_NOINFO varchar(1) NULL,
	CT_DSG varchar(10) NULL,
	CT_REGISTERSHOWS varchar(75) NULL,
	CT_REGT varchar(40) NULL,
	CT_NBROFBURIALS float NULL,
	CT_FINI varchar(1) NULL,
	CT_FOLDER varchar(1) NULL,
	CT_ID float PRIMARY KEY
	);


CREATE TABLE IF NOT EXISTS Company_Std (
	Comp_Name_Orig varchar(7) NULL,
	Comp_Name_Std varchar(7) NOT NULL,
	Comp_Isdelete bit NOT NULL,
	Comp_PubDate datetime NOT NULL,
	Comp_UpdateDate datetime NULL,
	Comp_UpdateBy int NULL,
	Comp_UpdateType varchar(15) NULL,
	Comp_Comments varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS Contitle (
	STATE varchar(3) PRIMARY KEY,
	SIDE varchar(2),
	TITLE varchar(50),
	ISDELETE bit NOT NULL,
	PUBDATE datetime NOT NULL,
	UPDATEDATE datetime,
	UPDATEBY int,
	UPDATETYPE varchar(15),
	COMMENTS varchar(255)
	);

-- CREATE TABLE focus (
-- 	id int PRIMARY KEY,
-- 	datecreated varchar(200) NULL,
-- 	coveragetemporal varchar(500) NULL,
-- 	begindate varchar(50) NULL,
-- 	enddate varchar(50) NULL,
-- 	relation varchar(500) NULL,
-- 	url varchar(500) NULL,
-- 	mrsid1 varchar(5) NULL,
-- 	server1 varchar(150) NULL,
-- 	catalog1 varchar(150) NULL,
-- 	file1 varchar(150) NULL,
-- 	folder1 varchar(150) NULL,
-- 	part1 varchar(150) NULL,
-- 	sourceproperties1 varchar(5) NULL,
-- 	format1 varchar(100) NULL,
-- 	filesize1 varchar(5) NULL,
-- 	width1 varchar(10) NULL,
-- 	height1 varchar(10) NULL,
-- 	bitdepth1 varchar(10) NULL,
-- 	mrsid2 varchar(5) NULL,
-- 	server2 varchar(150) NULL,
-- 	catalog2 varchar(150) NULL,
-- 	file2 varchar(150) NULL,
-- 	folder2 varchar(150) NULL,
-- 	part2 varchar(150) NULL,
-- 	sourceproperties2 varchar(5) NULL,
-- 	format2 varchar(100) NULL,
-- 	filesize2 varchar(5) NULL,
-- 	width2 varchar(10) NULL,
-- 	height2 varchar(10) NULL,
-- 	bitdepth2 varchar(10) NULL,
-- 	mrsid3 varchar(5) NULL,
-- 	server3 varchar(150) NULL,
-- 	catalog3 varchar(150) NULL,
-- 	file3 varchar(150) NULL,
-- 	folder3 varchar(150) NULL,
-- 	part3 varchar(150) NULL,
-- 	sourceproperties3 varchar(5) NULL,
-- 	format3 varchar(100) NULL,
-- 	filesize3 varchar(5) NULL,
-- 	width3 varchar(10) NULL,
-- 	height3 varchar(10) NULL,
-- 	bitdepth3 varchar(10) NULL,
-- 	mrsid4 varchar(5) NULL,
-- 	server4 varchar(150) NULL,
-- 	catalog4 varchar(150) NULL,
-- 	file4 varchar(150) NULL,
-- 	folder4 varchar(150) NULL,
-- 	part4 varchar(150) NULL,
-- 	sourceproperties4 varchar(5) NULL,
-- 	format4 varchar(100) NULL,
-- 	filesize4 varchar(5) NULL,
-- 	width4 varchar(10) NULL,
-- 	height4 varchar(10) NULL,
-- 	bitdepth4 varchar(10) NULL,
-- 	rights varchar(200) NULL,
-- 	rightsinfo varchar(1500) NULL,
-- 	title varchar(500) NULL,
-- 	contributor1 varchar(200) NULL,
-- 	affiliation1 varchar(200) NULL,
-- 	role1 varchar(200) NULL,
-- 	contributor2 varchar(200) NULL,
-- 	affiliation2 varchar(200) NULL,
-- 	role2 varchar(200) NULL,
-- 	contributor3 varchar(200) NULL,
-- 	affiliation3 varchar(200) NULL,
-- 	role3 varchar(200) NULL,
-- 	publisher varchar(250) NULL,
-- 	type varchar(200) NULL,
-- 	formatmedium varchar(250) NULL,
-- 	source varchar(400) NULL,
-- 	identifier varchar(400) NULL,
-- 	description1 varchar(2500) NULL,
-- 	description2 varchar(2500) NULL,
-- 	description3 varchar(2500) NULL,
-- 	description4 varchar(2500) NULL,
-- 	subject1 varchar(150) NULL,
-- 	subject2 varchar(150) NULL,
-- 	subject3 varchar(150) NULL,
-- 	subject4 varchar(150) NULL,
-- 	subject5 varchar(150) NULL,
-- 	subject6 varchar(150) NULL,
-- 	parkname varchar(300) NULL,
-- 	parkcode varchar(10) NULL,
-- 	coveragespatial varchar(500) NULL,
-- 	north varchar(50) NULL,
-- 	west varchar(50) NULL,
-- 	abstract varchar(8000) NULL,
-- 	descriptionabstract varchar(8000) NULL,
-- 	relationispartof1 varchar(250) NULL,
-- 	relationispartof2 varchar(250) NULL,
-- 	relationispartof3 varchar(250) NULL,
-- 	relationispartof4 varchar(250) NULL,
-- 	recordstate varchar(100) NULL,
-- 	recordowner varchar(200) NULL,
-- 	recordview varchar(55) NULL,
-- 	recorduid varchar(50) NULL,
-- 	recordsetuid varchar(50) NULL,
-- 	useruid varchar(50) NULL,
-- 	batcreatedate varchar(50) NULL,
-- 	batmodifydate varchar(50) NULL,
-- 	stateuid varchar(50) NULL,
-- 	tableofcontents varchar(1000) NULL,
-- 	subjectkeyword varchar(1500) NULL,
-- 	titlealternative varchar(500) NULL,
-- 	npsnumber varchar(250) NULL,
-- 	yyyymmdd varchar(10) NULL,
-- 	numbertype varchar(100) NULL,
-- 	djvu varchar(100) NULL,
-- 	file varchar(100) NULL,
-- 	folder varchar(100) NULL,
-- 	format varchar(100) NULL,
-- 	identifierurl varchar(200) NULL,
-- 	language varchar(100) NULL,
-- 	server varchar(100) NULL,
-- 	catalog varchar(100) NULL,
-- 	descriptiontableofcontents varchar(500) NULL
-- );


CREATE TABLE IF NOT EXISTS Medal_Ofhonor (
	MD_LASTNAME varchar(15) NULL,
	MD_FIRSTNAME varchar(20) NULL,
	MD_RANKCODE varchar(8) NULL,
	MD_CO varchar(1) NULL,
	MD_UNITNAME varchar(50) NULL,
	MD_CITATIONCITY varchar(15) NULL,
	MD_CITATIONSTATE varchar(2) NULL,
	MD_CITATIONDATE varchar(12) NULL,
	MD_ENTERPL varchar(15) NULL,
	MD_ENTERST varchar(9) NULL,
	MD_BIRTHPL varchar(15) NULL,
	MD_ISSUEDX varchar(12) NULL,
	MD_PAGE varchar(3) NULL,
	MD_CWUNIT varchar(12) NULL,
	MD_RECNUMBER numeric(11, 0) PRIMARY KEY,
	MD_CITATION varchar(2000) NULL,
	MD_BIRTHST varchar(7) NULL,
	MD_SIDE varchar(1) NULL,
	MD_BRANCHOFSERVICE varchar(30) NULL,
	MD_MIDDLEINITIAL varchar(7) NULL,
	MD_ISDELETE bit NOT NULL,
	MD_PUBDATE datetime NOT NULL,
	MD_UPDATEDATE datetime NULL,
	MD_UPDATEBY int NULL,
	MD_UPDATETYPE varchar(15) NULL,
	MD_COMMENTS varchar(255) NULL
	);

CREATE TABLE Medal_Ofhonor_unusedColumns(
	MD_RECNUMBER numeric(11, 0) PRIMARY KEY,
	MD_X varchar(1) NULL,
	MD_DATE_R datetime NULL,
	MD_ISSUED datetime NULL,
	MD_M varchar(4) NULL,
	MD_D varchar(3) NULL,
	MD_Y varchar(5) NULL,
	MD_CITATION1 varchar(60) NULL,
	MD_CITATION2 varchar(60) NULL,
	MD_CITATION3 varchar(60) NULL,
	MD_CITATION4 varchar(60) NULL,
	MD_CITATION5 varchar(60) NULL,
	MD_CITATION6 varchar(60) NULL,
	MD_CITATION7 varchar(60) NULL,
	MD_CITATION8 varchar(60) NULL,
	MD_RUNNING float NULL,
	MD_MIDDLEINITIAL varchar(7) NULL
);

CREATE TABLE MEMORIAL (
	MEM_NBR float NULL,
	MEM_GIV_NAME_ORIG varchar(50) NULL,
	MEM_SUR_NAME_ORIG varchar(30) NULL,
	MEM_UNIT_CODE varchar(12) NULL,
	MEM_AKA_NAME_ORIG varchar(50) NULL,
	MEM_NAME_DUP varchar(3) NULL,
	MEM_NAME_DUP_PTR float NULL,
	MEM_NAME_SEP_CHAR varchar(1) NULL,
	MEM_AKA_SUR_NAME varchar(50) NULL,
	MEM_AKA_GIV_NAME varchar(50) NULL,
	MEM_GIV_NAME_FULL varchar(50) NULL,
	MEM_AKA_GIV_FULL varchar(50) NULL,
	MEM_PLAQUE_ID varchar(5) NULL,
	MEM_NBR_ORIG float NULL,
	MEM_ISDELETE bit NOT NULL,
	MEM_PUBDATE datetime NOT NULL,
	MEM_UPDATEDATE datetime NULL,
	MEM_UPDATEBY int NULL,
	MEM_UPDATETYPE varchar(15) NULL,
	MEM_COMMENTS varchar(255) NULL
);

CREATE TABLE Prisoners_Andersonville(
	PRA_LASTNAME varchar(15) NULL,
	PRA_FIRSTNAME varchar(13) NULL,
	PRA_STATE varchar(3) NULL,
	PRA_REGIMENT varchar(3) NULL,
	PRA_RANK varchar(10) NULL,
	PRA_COMPANY varchar(1) NULL,
	PRA_FUNCTION varchar(15) NULL,
	PRA_CODE varchar(5) NULL,
	PRA_REMARKS varchar(255) NULL,
	PRA_ALTNAME1 varchar(13) NULL,
	PRA_ALTNAME2 varchar(13) NULL,
	PRA_ALTNAME3 varchar(13) NULL,
	PRA_ALTNAME4 varchar(13) NULL,
	PRA_UNITNAME varchar(35) NULL,
	PRA_STATENAME varchar(20) NULL,
	PRA_SIDE varchar(1) NULL,
	PRA_CAPTURE varchar(20) NULL,
	PRA_DCAP datetime NULL,
	PRA_TYPEDESCRIPTION varchar(120) NULL,
	PRA_ISDELETE bit NOT NULL,
	PRA_PUBDATE datetime NOT NULL,
	PRA_UPDATEDATE datetime NULL,
	PRA_UPDATEBY int NULL,
	PRA_UPDATETYPE varchar(15) NULL,
	PRA_COMMENTS varchar(255) NULL,
	PRA_PKEY int PRIMARY KEY
);


CREATE TABLE Prisoners_Andersonville_unusedColumns (
	PRA_PKEY PRIMARY KEY,
	PRA_GRAVE varchar(5) NULL,
	PRA_DCAUSE varchar(18) NULL,
	PRA_DDATE datetime NULL,
	PRA_REF varchar(75) NULL,
	PRA_CAPTURE varchar(20) NULL,
	PRA_DCAP datetime NULL,
	PRA_PG numeric(5, 0) NULL,
	PRA_MORE varchar(3) NULL,
	PRA_TOTAL numeric(2, 0) NULL
);


CREATE TABLE Prisoners_FtCode(
	CODE varchar(10) NOT NULL,
	DISPOSITION varchar(25) NULL,
	Ft_DESCRIPTION varchar(10) NOT NULL,
	FT_ISDELETE bit NOT NULL,
	FT_PUBDATE datetime NOT NULL,
	FT_UPDATEDATE datetime NULL,
	FT_UPDATEBY int NULL,
	FT_UPDATETYPE varchar(15) NULL,
	FT_COMMENTS varchar(255) NULL,
	PRIMARY KEY (CODE, Ft_DESCRIPTION)
	);

CREATE TABLE Prisoners_FtMcHenry(
	PRM_TYPE varchar(2) NULL,
	PRM_NAME varchar(20) NULL,
	PRM_REGISTRATIONDATE datetime NULL,
	PRM_RESIDENCE varchar(15) NULL,
	PRM_DATEDISP datetime NULL,
	PRM_DISP varchar(4) NULL,
	PRM_HOSPITAL varchar(2) NULL,
	PRM_FTRANK varchar(2) NULL,
	PRM_NOTES varchar(30) NULL,
	PRM_LASTNAME varchar(50) NULL,
	PRM_FIRSTNAME varchar(50) NULL,
	PRM_RECNUMBER float NULL,
	PRM_ID int PRIMARY KEY,
	PRM_TYPEDESCRIPTION varchar(50) NULL,
	PRM_ISDELETE bit NOT NULL,
	PRM_PUBDATE datetime NOT NULL,
	PRM_UPDATEDATE datetime NULL,
	PRM_UPDATEBY int NULL,
	PRM_UPDATETYPE varchar(15) NULL,
	PRM_COMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS Rankz (
	RANK_CODE varchar(4) NOT NULL,
	RANK_NAME varchar(54),
	RANK_ISDELETE bit NOT NULL,
	RANK_PUBDATE datetime NOT NULL,
	RANK_UPDATEDATE datetime,
	RANK_UPDATETYPE varchar(15),
	RANK_COMMENTS varchar(255),
	RANK_UPDATEBY int
	);


CREATE TABLE IF NOT EXISTS Regiments_Unitz (
	REG_UNIT_CODE varchar(12) PRIMARY KEY NOT NULL,
	REG_SIDE varchar(1) NOT NULL,
	REG_STATE varchar(2) NOT NULL,
	REG_ORDINAL varchar(4) NOT NULL,
	REG_ARM varchar(1),
	REG_TYPE varchar(1),
	REG_SPECIAL varchar(1),
	REG_DUPLICATE varchar(1),
	REG_ETHNIC varchar(1),
	REG_HISTORY text,
	REG_UNIT_NAME varchar(110),
	REG_NOTES varchar(200),
	REG_FUNCTION varchar(2),
	REG_LONGHISTORY text,
	REG_ISDELETE bit NOT NULL,
	REG_PUBDATE datetime NOT NULL,
	REG_UPDATEDATE datetime,
	REG_UPDATEBY int,
	REG_COMMENTS varchar(255),
	REG_UPDATETYPE varchar(15)
	);


CREATE TABLE IF NOT EXISTS Regiments_Unitz_Ext (
	REG_UNIT_CODE varchar(12) PRIMARY KEY,
	REG_DUPLICATE varchar(1) NULL,
	REG_ORG_CITY varchar(25) NULL,
	REG_ORG_COUNTY varchar(25) NULL,
	REG_ORG_STATE varchar(2) NULL,
	REG_ORG_DATE datetime NULL,
	REG_EISDELETE bit NOT NULL,
	REG_EPUBDATE datetime NOT NULL,
	REG_EUPDATEDATE datetime NULL,
	REG_EUPDATEBY int NULL,
	REG_EUPDATETYPE varchar(15) NULL,
	REG_ECOMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS SAILORS_CONTISLANDS(
	PKID varchar(255),
	CONTISLANDNAMES varchar(255),
	COUNTRYABBR varchar(255)
	);

CREATE TABLE IF NOT EXISTS Sailors_Enlistinfo(
	SAL_ENLISTID varchar(7) PRIMARY KEY,
	SAL_DATEENLIST datetime NULL,
	SAL_RATING varchar(24) NULL,
	SAL_PLACENLIST varchar(30) NULL,
	SAL_REENLIST varchar(50) NULL,
	SAL_TERMENLIST varchar(5) NULL,
	SAL_EISDELETE bit NOT NULL,
	SAL_EPUBDATE datetime NOT NULL,
	SAL_EUPDATEDATE datetime NULL,
	SAL_EUPDATEBY int NULL,
	SAL_EUPDATETYPE varchar(15) NULL,
	SAL_ECOMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS Sailors_Musterinfo(
	SAL_DATEMUSTER datetime NULL,
	SAL_MUSTERID varchar(7) NULL,
	SAL_VESSEL varchar(20) NULL,
	SAL_PKID int PRIMARY KEY,
	SAL_MISDELETE bit NOT NULL,
	SAL_MPUBDATE datetime NOT NULL,
	SAL_MUPDATEDATE datetime NULL,
	SAL_MUPDATEBY int NULL,
	SAL_MUPDATETYPE varchar(15) NULL,
	SAL_MCOMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS Sailors_Personinfo(
	SAL_INFOID varchar(7) PRIMARY KEY,
	SAL_LASTNAME varchar(15) NULL,
	SAL_FIRSTNAME varchar(20) NULL,
	SAL_MIDDLENAME varchar(10) NULL,
	SAL_CITYOFBIRTH varchar(20) NULL,
	SAL_STATEOFBIRTH varchar(18) NULL,
	SAL_AGE varchar(22) NULL,
	SAL_OCCUPATION varchar(30) NULL,
	SAL_COMPLEXION varchar(15) NULL,
	SAL_HEIGHTFEET varchar(22) NULL,
	SAL_HEIGHTINCH varchar(22) NULL,
	SAL_COUNTRYOFBIRTH varchar(18) NULL,
	SAL_ISDELETE bit NOT NULL,
	SAL_PUBDATE datetime NOT NULL,
	SAL_UPDATEDATE datetime NULL,
	SAL_UPDATEBY int NULL,
	SAL_UPDATETYPE varchar(15) NULL,
	SAL_COMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS Sailors_Shipinfo (
	SAl_VESSEL varchar(20) NULL,
	SAL_PKID int PRIMARY KEY,
	SAL_SISDELETE bit NOT NULL,
	SAL_SPUBDATE datetime NOT NULL,
	SAL_SUPDATE datetime NULL,
	SAL_SUPDATEBY int NULL,
	SAL_SUPDATETYPE varchar(15) NULL,
	SAL_SCOMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS SoldiersCountPerState(
	StateAbbr char(3) PRIMARY KEY,
	UnionCount int NULL,
	ConfederateCount int NULL,
	TotalCount int NULL
	);

CREATE TABLE Soldiers_Filmz(
	FILM_NBR varchar(7) PRIMARY KEY,
	FILM_ROLL varchar(15) NULL,
	FILM_ISDELETE bit NOT NULL,
	FILM_PUBDATE datetime NOT NULL,
	FILM_UPDATEDATE datetime NULL,
	FILM_UPDATEBY int NULL,
	FILM_UPDATETYPE varchar(15) NULL,
	FILM_COMMENTS varchar(255) NULL
	);

CREATE TABLE Soldiers_Memorial(
	MEM_NBR_ORIG float PRIMARY KEY,
	MEM_NAME_DUP varchar(3) NULL,
	MEM_NAME_DUP_PTR float NULL,
	MEM_NAME_SEP_CHAR varchar(1) NULL,
	MEM_AKA_SUR_NAME varchar(50) NULL,
	MEM_AKA_GIV_NAME varchar(50) NULL,
	MEM_GIV_NAME_FULL varchar(50) NULL,
	MEM_AKA_GIV_FULL varchar(50) NULL,
	MEM_PLAQUE_ID varchar(5) NULL,
	MEM_PK varchar(50) NULL,
	MEM_SUR_NAME_ORIG varchar(30) NULL,
	MEM_ISDELETE bit NOT NULL,
	MEM_PUBDATE datetime NOT NULL,
	MEM_UPDATEDATE datetime NULL,
	MEM_UPDATEBY int NULL,
	MEM_UPDATETYPE varchar(15) NULL,
	MEM_COMMENTS varchar(255) NULL
	);

CREATE TABLE Soldiers_Memorial_backup (
	MEM_NBR_ORIG float PRIMARY KEY,
	MEM_NAME_DUP varchar(3) NULL,
	MEM_NAME_DUP_PTR float NULL,
	MEM_NAME_SEP_CHAR varchar(1) NULL,
	MEM_AKA_SUR_NAME varchar(50) NULL,
	MEM_AKA_GIV_NAME varchar(50) NULL,
	MEM_GIV_NAME_FULL varchar(50) NULL,
	MEM_AKA_GIV_FULL varchar(50) NULL,
	MEM_PLAQUE_ID varchar(5) NULL,
	MEM_PK varchar(50) NULL
	);


CREATE TABLE IF NOT EXISTS Soldiers_notez (
	PER_NBR_ORIG float PRIMARY KEY,
	PER_NOTES varchar NULL,
	PER_NAMENOTE varchar NULL,
	PER_COMPANYNOTE varchar NULL,
	PER_UNITNOTE varchar NULL,
	PER_SIDENOTE varchar NULL,
	PER_RANKINNOTE varchar NULL,
	PER_RANKOUTNOTE varchar NULL,
	PER_AKANOTE varchar NULL,
	PER_PK varchar(50) NULL,
	PER_NISDELETE bit NOT NULL,
	PER_NPUBDATE datetime NOT NULL,
	PER_NUPDATEDATE datetime NULL,
	PER_NUPDATEBY int NULL,
	PER_NUPDATETYPE varchar(15) NULL,
	PER_NCOMMENTS varchar(255) NULL
	);


CREATE TABLE IF NOT EXISTS Soldiers_Personz (
	PER_FIRST_NAME varchar(50) NULL,
	PER_LAST_NAME varchar(40) NULL,
	PER_SIDE varchar(1) NULL,
	PER_UNIT_ORIG varchar(340) NULL,
	PER_UNIT_CODE varchar(12) NULL,
	PER_COMPANY varchar(3) NULL,
	PER_RANK_IN_ORIG varchar(60) NULL,
	PER_RANK_IN_CODE varchar(4) NULL,
	PER_RANK_OUT_ORIG varchar(60) NULL,
	PER_RANK_OUT_CODE varchar(4) NULL,
	PER_AKA_NAME_ORIG varchar(140) NULL,
	PER_BAT_NBR varchar(8) NULL,
	PER_FILM_NBR varchar(7) NULL,
	PER_NBR_ORIG float NOT NULL,
	PER_STATE varchar(2) NULL,
	PER_FUNCTION varchar(2) NULL,
	PER_UNIT_NUMBER varchar(4) NULL,
	PER_PK uniqueidentifier PRIMARY KEY,
	PER_ISDELETE bit NOT NULL,
	PER_PUBDATE datetime NOT NULL,
	PER_UPDATEDATE datetime NULL,
	PER_UPDATEBY int NULL,
	PER_UPDATETYPE varchar(15) NULL,
	PER_COMMENTS varchar(255) NULL
	);

CREATE TABLE StateCountryName(
	State_Country varchar(25) NULL,
	STATECOUNTRY_ABBR varchar(5) PRIMARY KEY,
	COLUMN_ABBR varchar(70) NULL,
	COLUMN_ABBRDESCRIPTION varchar(150) NULL,
	PK_ID int IDENTITY(1,1) NOT NULL,
	NAME varchar(50) NULL,
	SC_ISDELETE bit NOT NULL,
	SC_PUBDATE datetime NOT NULL,
	SC_UPDATEDATE datetime NULL,
	SC_UPDATEBY int NULL,
	SC_UPDATETYPE varchar(15) NULL,
	SC_COMMENTS varchar(255) NULL
	);

CREATE TABLE IF NOT EXISTS State_Name (
	STATE_ABBR varchar(10) PRIMARY KEY NOT NULL,
	STATE_NAME varchar(150) ,
	STATE_ISDELETE bit NOT NULL,
	STATE_PUBDATE datetime NOT NULL,
	STATE_UPDATEDATE datetime,
	STATE_UPDATEBY int,
	STATE_UPDATETYPE varchar(15),
	STATE_COMMENTS varchar(255)
	);

-- Ignore sysdiagrams
	
CREATE TABLE IF NOT EXISTS Unititle (
	STATE varchar(3) PRIMARY KEY,
	SIDE varchar(2),
	TITLE varchar(50),
	ISDELETE bit NOT NULL,
	PUBDATE datetime NOT NULL,
	UPDATEDATE datetime,
	UPDATEBY int,
	UPDATETYPE varchar(15),
	COMMENTS varchar(255)
	);
