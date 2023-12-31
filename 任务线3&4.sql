USE [plant]
GO
/****** Object:  Table [dbo].[病虫害]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[病虫害](
	[病虫害id] [int] NOT NULL,
	[病虫害名称] [nchar](20) NULL,
	[作用期限] [datetime] NULL,
	[防治方法] [nchar](100) NULL,
 CONSTRAINT [PK_病虫害] PRIMARY KEY CLUSTERED 
(
	[病虫害id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[防治]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[防治](
	[病虫害id] [int] NOT NULL,
	[药物id] [int] NOT NULL,
 CONSTRAINT [PK_防治] PRIMARY KEY CLUSTERED 
(
	[病虫害id] ASC,
	[药物id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[患病]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[患病](
	[植物编号] [int] NOT NULL,
	[病虫害id] [int] NOT NULL,
 CONSTRAINT [PK_患病] PRIMARY KEY CLUSTERED 
(
	[植物编号] ASC,
	[病虫害id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[养护]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[养护](
	[植物编号] [int] NOT NULL,
	[任务编号] [int] NOT NULL,
	[执行时间] [datetime] NULL,
	[执行地点] [nchar](50) NULL,
	[执行人员] [nchar](10) NULL,
 CONSTRAINT [PK_养护] PRIMARY KEY CLUSTERED 
(
	[植物编号] ASC,
	[任务编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[养护任务]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[养护任务](
	[任务编号] [int] NOT NULL,
	[养护任务名称] [nchar](20) NULL,
	[任务描述] [nchar](100) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[药物]    Script Date: 2023/12/25 17:33:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[药物](
	[药物id] [int] NOT NULL,
	[药剂名称] [nchar](20) NULL,
	[药剂用量] [float] NULL,
 CONSTRAINT [PK_药物] PRIMARY KEY CLUSTERED 
(
	[药物id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[防治]  WITH CHECK ADD  CONSTRAINT [FK_防治_病虫害] FOREIGN KEY([病虫害id])
REFERENCES [dbo].[病虫害] ([病虫害id])
GO
ALTER TABLE [dbo].[防治] CHECK CONSTRAINT [FK_防治_病虫害]
GO
ALTER TABLE [dbo].[防治]  WITH CHECK ADD  CONSTRAINT [FK_防治_药物] FOREIGN KEY([药物id])
REFERENCES [dbo].[药物] ([药物id])
GO
ALTER TABLE [dbo].[防治] CHECK CONSTRAINT [FK_防治_药物]
GO
ALTER TABLE [dbo].[患病]  WITH CHECK ADD  CONSTRAINT [FK_患病_患病] FOREIGN KEY([植物编号], [病虫害id])
REFERENCES [dbo].[患病] ([植物编号], [病虫害id])
GO
ALTER TABLE [dbo].[患病] CHECK CONSTRAINT [FK_患病_患病]
GO
ALTER TABLE [dbo].[患病]  WITH CHECK ADD  CONSTRAINT [FK_患病_植物信息] FOREIGN KEY([植物编号])
REFERENCES [dbo].[植物信息] ([植物编号])
GO
ALTER TABLE [dbo].[患病] CHECK CONSTRAINT [FK_患病_植物信息]
GO
