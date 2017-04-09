import gpxpy, os, mplleaflet
import matplotlib.pyplot as plt
import time

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

                for i in range(0, len(segment.points), 10):
                    lat.append(segment.points[i].latitude)a
                    lon.append(segment.points[i].longitude)

        plt.plot(lon, lat, color=colour, lw=3, alpha=0.5)
    print(dir + ' plotted')

# init plot
fig = plt.figure(facecolor='0.1')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)
# show plot
plotGPX('../joeGPX', 'red')
plotGPX('../gabGPX', 'mediumvioletred')
plotGPX('../scoGPX', 'orange')
plotGPX('../adamGPX', 'darkgreen')

mplleaflet.save_html(fig, '../maps/'+str(int(time.time())) + '.html')

plt.show()

# plt.savefig('output.png', facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=500)
