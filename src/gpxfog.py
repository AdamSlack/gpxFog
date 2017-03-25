import gpxpy, os, mplleaflet
import matplotlib.pyplot as plt

def parseGPX(dir):
    # reading GPX files.
    fileList = os.listdir(dir)
    gpxData = []

    for f in fileList:
        gpx = open(dir + '/' + f, 'r')
        gpxData.append(gpxpy.parse(gpx))

    print(dir + ' Parsed')
    lat = []
    lon = []

    # plot data
    for gpx in gpxData:

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lat.append(point.latitude)
                    lon.append(point.longitude)

    return lat, lon

def drawGPX(lat, lon, colour):
    plt.plot(lon, lat, color=colour, lw=1, alpha=1)


def plotGPX(dir, colour):
    # reading GPX files.
    fileList = os.listdir(dir)
    gpxData = []

    for f in fileList:
       gpx = open(dir + '/' + f, 'r')
       gpxData.append(gpxpy.parse(gpx))

    print(dir + ' Parsed')
    # plot data
    for gpx in gpxData:
        lat = []
        lon = []

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lat.append(point.latitude)
                    lon.append(point.longitude)

        plt.plot(lon, lat, color=colour, lw=3, alpha=0.8)
    print(dir + ' plotted')

# init plot
fig = plt.figure(facecolor='0.1')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)

# show plot
plotGPX('../adamGPX', 'blue')
plotGPX('../joeGPX', 'red')
plotGPX('../gabGPX', 'mediumvioletred')
plotGPX('../scoGPX', 'orange')

mplleaflet.show(fig,)

plt.show()

plt.savefig('output.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=500)
