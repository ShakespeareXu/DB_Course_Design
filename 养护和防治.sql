USE [plant]
GO
/****** Object:  Table [dbo].[病虫害]    Script Date: 2023/12/25 15:51:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[病虫害](
	[病虫害id] [nchar](10) NOT NULL,
	[病虫害名称] [nchar](10) NOT NULL,
	[作用期限] [datetime] NULL,
	[防治方法] [nchar](10) NULL,
 CONSTRAINT [PK_病虫害] PRIMARY KEY CLUSTERED 
(
	[病虫害id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[养护]    Script Date: 2023/12/25 15:51:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[养护](
	[植物编号] [nchar](10) NOT NULL,
	[任务编号] [nchar](10) NOT NULL,
	[执行时间] [datetime] NULL,
	[执行地点] [nchar](10) NULL,
	[执行人员] [nchar](10) NULL,
 CONSTRAINT [PK_养护] PRIMARY KEY CLUSTERED 
(
	[植物编号] ASC,
	[任务编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[养护任务]    Script Date: 2023/12/25 15:51:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[养护任务](
	[任务编号] [nchar](10) NOT NULL,
	[养护任务名称] [nchar](10) NULL,
	[任务描述] [nchar](50) NULL,
 CONSTRAINT [PK_养护任务] PRIMARY KEY CLUSTERED 
(
	[任务编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[药物]    Script Date: 2023/12/25 15:51:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[药物](
	[药物id] [nchar](10) NOT NULL,
	[药剂名称] [nchar](20) NOT NULL,
	[药剂用量] [float] NULL,
 CONSTRAINT [PK_药物] PRIMARY KEY CLUSTERED 
(
	[药物id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
