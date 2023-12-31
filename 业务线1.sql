USE [plant]
GO
/****** Object:  Table [dbo].[科]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[科](
	[科ID] [int] NOT NULL,
	[科名] [nchar](10) NULL,
 CONSTRAINT [PK_科] PRIMARY KEY CLUSTERED 
(
	[科ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[配图]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[配图](
	[配图编号] [int] NOT NULL,
	[配图拍摄地点] [nchar](100) NULL,
	[配图描述] [nchar](100) NULL,
	[配图拍摄人] [nchar](100) NULL,
	[配图存储路径] [nchar](100) NULL,
 CONSTRAINT [PK_配图] PRIMARY KEY CLUSTERED 
(
	[配图编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[配有]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[配有](
	[植物编号] [int] NULL,
	[配图编号] [int] NOT NULL,
 CONSTRAINT [PK_配有] PRIMARY KEY CLUSTERED 
(
	[配图编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[植物信息]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[植物信息](
	[植物名称] [nchar](10) NULL,
	[植物编号] [int] NOT NULL,
 CONSTRAINT [PK_植物信息] PRIMARY KEY CLUSTERED 
(
	[植物编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[种]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[种](
	[种ID] [int] NOT NULL,
	[种名] [nchar](100) NULL,
	[应用价值] [nchar](100) NULL,
	[形态特征] [nchar](100) NULL,
	[栽培要点] [nchar](100) NULL,
	[生长环境] [nchar](100) NULL,
	[病名] [nchar](100) NULL,
	[别名] [nchar](100) NULL,
 CONSTRAINT [PK_种] PRIMARY KEY CLUSTERED 
(
	[种ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[属]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[属](
	[属ID] [int] NOT NULL,
	[属名] [nchar](100) NULL,
 CONSTRAINT [PK_属] PRIMARY KEY CLUSTERED 
(
	[属ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[属于科属]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[属于科属](
	[属ID] [int] NOT NULL,
	[科ID] [int] NULL,
 CONSTRAINT [PK_属于科属] PRIMARY KEY CLUSTERED 
(
	[属ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[属于植物信息]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[属于植物信息](
	[植物编号] [int] NOT NULL,
	[种ID] [int] NULL,
 CONSTRAINT [PK_属于植物信息] PRIMARY KEY CLUSTERED 
(
	[植物编号] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[属于属种]    Script Date: 2023/12/25 16:30:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[属于属种](
	[属ID] [int] NULL,
	[种ID] [int] NOT NULL,
 CONSTRAINT [PK_属于属种] PRIMARY KEY CLUSTERED 
(
	[种ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
ALTER TABLE [dbo].[配有]  WITH CHECK ADD  CONSTRAINT [FK_配有_配图] FOREIGN KEY([配图编号])
REFERENCES [dbo].[配图] ([配图编号])
GO
ALTER TABLE [dbo].[配有] CHECK CONSTRAINT [FK_配有_配图]
GO
ALTER TABLE [dbo].[配有]  WITH CHECK ADD  CONSTRAINT [FK_配有_植物信息] FOREIGN KEY([植物编号])
REFERENCES [dbo].[植物信息] ([植物编号])
GO
ALTER TABLE [dbo].[配有] CHECK CONSTRAINT [FK_配有_植物信息]
GO
ALTER TABLE [dbo].[属于科属]  WITH CHECK ADD  CONSTRAINT [FK_属于科属_科] FOREIGN KEY([科ID])
REFERENCES [dbo].[科] ([科ID])
GO
ALTER TABLE [dbo].[属于科属] CHECK CONSTRAINT [FK_属于科属_科]
GO
ALTER TABLE [dbo].[属于科属]  WITH CHECK ADD  CONSTRAINT [FK_属于科属_属] FOREIGN KEY([属ID])
REFERENCES [dbo].[属] ([属ID])
GO
ALTER TABLE [dbo].[属于科属] CHECK CONSTRAINT [FK_属于科属_属]
GO
ALTER TABLE [dbo].[属于植物信息]  WITH CHECK ADD  CONSTRAINT [FK_BelongsTo_PlantInfo] FOREIGN KEY([植物编号])
REFERENCES [dbo].[植物信息] ([植物编号])
GO
ALTER TABLE [dbo].[属于植物信息] CHECK CONSTRAINT [FK_BelongsTo_PlantInfo]
GO
ALTER TABLE [dbo].[属于植物信息]  WITH CHECK ADD  CONSTRAINT [FK_BelongsTo_Species] FOREIGN KEY([种ID])
REFERENCES [dbo].[种] ([种ID])
GO
ALTER TABLE [dbo].[属于植物信息] CHECK CONSTRAINT [FK_BelongsTo_Species]
GO
ALTER TABLE [dbo].[属于属种]  WITH CHECK ADD  CONSTRAINT [FK_属于属种_属] FOREIGN KEY([属ID])
REFERENCES [dbo].[属] ([属ID])
GO
ALTER TABLE [dbo].[属于属种] CHECK CONSTRAINT [FK_属于属种_属]
GO
ALTER TABLE [dbo].[属于属种]  WITH CHECK ADD  CONSTRAINT [FK_属于属种_种] FOREIGN KEY([种ID])
REFERENCES [dbo].[种] ([种ID])
GO
ALTER TABLE [dbo].[属于属种] CHECK CONSTRAINT [FK_属于属种_种]
GO
