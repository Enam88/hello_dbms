CREATE TABLE [dbo].[world] (
    [Country]                          NVARCHAR (50) NOT NULL,
    [Region]                           NVARCHAR (50) NOT NULL,
    [Population]                       INT           NOT NULL,
    [Area_sq_mi]                       INT           NOT NULL,
    [Pop_Density_per_sq_mi]            FLOAT (53)    NOT NULL,
    [Coastline_coast_area_ratio]       FLOAT (53)    NOT NULL,
    [Net_migration]                    FLOAT (53)    NULL,
    [Infant_mortality_per_1000_births] FLOAT (53)    NULL,
    [GDP_per_capita]                   INT           NULL,
    [Literacy]                         FLOAT (53)    NULL,
    [Phones_per_1000]                  FLOAT (53)    NULL,
    [Arable]                           FLOAT (53)    NULL,
    [Crops]                            FLOAT (53)    NULL,
    [Other]                            FLOAT (53)    NULL,
    [Climate]                          FLOAT (53)    NULL,
    [Birthrate]                        FLOAT (53)    NULL,
    [Deathrate]                        FLOAT (53)    NULL,
    [Agriculture]                      FLOAT (53)    NULL,
    [Industry]                         FLOAT (53)    NULL,
    [Service]                          FLOAT (53)    NULL,
    CONSTRAINT [PK_countries] PRIMARY KEY CLUSTERED ([Country] ASC)
);


GO

